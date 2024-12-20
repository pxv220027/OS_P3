import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4337PRJ3"
MIN_DEGREE = 10
MAX_KEYS = 2 * MIN_DEGREE - 1

class BTreeNode:
    def __init__(self, block_id, is_leaf=True):
        self.block_id = block_id
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.child_block_ids = []

class BTree:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root_node = None
        self.next_block_id = 1

    def create_index_file(self):
        with open(self.file_path, 'wb') as file:
            magic_number = MAGIC_NUMBER
            root_block_id_bytes = (0).to_bytes(8, 'big')  # Root block ID (initially 0)
            next_block_id_bytes = (1).to_bytes(8, 'big')  # Next block ID (initially 1)
            header_bytes = magic_number + root_block_id_bytes + next_block_id_bytes
            file.write(header_bytes.ljust(BLOCK_SIZE, b'\x00'))
        print("Index file created.")

    def load_header(self):
        with open(self.file_path, 'rb') as file:
            header_bytes = file.read(BLOCK_SIZE)
            if header_bytes[:8] != MAGIC_NUMBER:
                raise ValueError("Invalid index file.")
            root_block_id = int.from_bytes(header_bytes[8:16], 'big')
            self.next_block_id = int.from_bytes(header_bytes[16:24], 'big')
            if root_block_id != 0:
                self.root_node = self.load_node(root_block_id)

    def save_header(self):
        with open(self.file_path, 'r+b') as file:
            magic_number = MAGIC_NUMBER
            root_block_id_bytes = (self.root_node.block_id if self.root_node else 0).to_bytes(8, 'big')
            next_block_id_bytes = self.next_block_id.to_bytes(8, 'big')
            header_bytes = magic_number + root_block_id_bytes + next_block_id_bytes
            file.write(header_bytes.ljust(BLOCK_SIZE, b'\x00'))

    def load_node(self, block_id):
        with open(self.file_path, 'rb') as file:
            file.seek(block_id * BLOCK_SIZE)
            block_data = file.read(BLOCK_SIZE)
        is_leaf = int.from_bytes(block_data[8:16], 'big') == 0
        keys = [int.from_bytes(block_data[24 + i * 8:32 + i * 8], 'big') for i in range(19)]
        values = [int.from_bytes(block_data[176 + i * 8:184 + i * 8], 'big') for i in range(19)]
        child_block_ids = [int.from_bytes(block_data[328 + i * 8:336 + i * 8], 'big') for i in range(20)]
        node = BTreeNode(block_id, is_leaf)
        node.keys = [key for key in keys if key != 0]
        node.values = [value for value in values if value != 0]
        node.child_block_ids = [child_id for child_id in child_block_ids if child_id != 0]
        return node

    def save_node(self, node):
        with open(self.file_path, 'r+b') as file:
            file.seek(node.block_id * BLOCK_SIZE)
            block_id_bytes = node.block_id.to_bytes(8, 'big')
            parent_block_id_bytes = (0 if node.is_leaf else node.block_id).to_bytes(8, 'big')
            key_count_bytes = len(node.keys).to_bytes(8, 'big')
            
            keys_bytes = b''.join(key.to_bytes(8, 'big') for key in node.keys)
            keys_padding = b'\x00' * (8 * (19 - len(node.keys)))
            
            values_bytes = b''.join(value.to_bytes(8, 'big') for value in node.values)
            values_padding = b'\x00' * (8 * (19 - len(node.values)))
            
            child_block_ids_bytes = b''.join(child_id.to_bytes(8, 'big') for child_id in node.child_block_ids)
            children_padding = b'\x00' * (8 * (20 - len(node.child_block_ids)))
            
            node_data = (
                block_id_bytes + 
                parent_block_id_bytes + 
                key_count_bytes + 
                keys_bytes + keys_padding + 
                values_bytes + values_padding + 
                child_block_ids_bytes + children_padding
            )
            
            file.write(node_data.ljust(BLOCK_SIZE, b'\x00'))

    def insert(self, key, value):
        if not self.root_node:
            self.root_node = BTreeNode(self.next_block_id)
            self.next_block_id += 1
            self.save_node(self.root_node)
        
        if key in self.root_node.keys:
            print(f"Key '{key}' already exists!")
            return
        
        inserted = False
        for i in range(len(self.root_node.keys)):
            if self.root_node.keys[i] > key:
                self.root_node.keys.insert(i, key)
                self.root_node.values.insert(i, value)
                inserted = True
                break

        if not inserted:
            self.root_node.keys.append(key)
            self.root_node.values.append(value)
        
        print(f"Inserted '{value}' at key '{key}'.")
        self.save_node(self.root_node)

    def search(self, key):
        if not self.root_node:
            return None
        current_node = self.root_node
        while current_node:
            if key in current_node.keys:
                key_index = current_node.keys.index(key)
                return current_node.values[key_index]
            elif current_node.is_leaf:
                break
            else:
                current_node = self.load_node(current_node.child_block_ids[0])  
        return None

    def print_tree(self):
        if not self.root_node:
            print("B-Tree is empty.")
            return
        self._print_node(self.root_node)

    def _print_node(self, node):
        for i in range(len(node.keys)):
            print(f"Key = '{node.keys[i]}', Value = '{node.values[i]}'")
        if not node.is_leaf:
            for child_block_id in node.child_block_ids:
                child_node = self.load_node(child_block_id)
                self._print_node(child_node)
    
    def extract_to_file(self, output_file_path):
        if not self.root_node:
            print("Error: No index file is open.")
            return
        
        if os.path.exists(output_file_path):
            overwrite = input(f"File '{output_file_path}' exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != "yes":
                print("Extract command aborted.")
                return
        
        try:
            with open(output_file_path, 'w') as output_file:
                self._write_node_to_file(self.root_node, output_file)
            print(f"Extracted all key-value pairs to '{output_file_path}'.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def _write_node_to_file(self, node, file):
        for i in range(len(node.keys)):
            file.write(f"{node.keys[i]},{node.values[i]}\n")
        if not node.is_leaf:
            for child_block_id in node.child_block_ids:
                child_node = self.load_node(child_block_id)
                self._write_node_to_file(child_node, file)

def main():
    current_btree = None
    while True:
        print("\n" + "=" * 40)
        print(" " * 12 + "COMMAND MENU")
        print("=" * 40)
        print("  create  - Create a new index file")
        print("  open    - Open an existing index file")
        print("  insert  - Insert a key-value pair")
        print("  search  - Search for a key")
        print("  load    - Load key-value pairs from a file")
        print("  print   - Print B-Tree structure")
        print("  extract - Save keys and values to a file")
        print("  quit    - Exit the program")
        print("=" * 40)

        command = input("Enter command: ").strip().lower()
        if command == "create":
            index_file_name = input("Enter index file name: ").strip()
            if os.path.exists(index_file_name):
                overwrite_confirmation = input("File exists. Overwrite? (yes/no): ").strip().lower()
                if overwrite_confirmation != "yes":
                    print("Create command aborted.")
                    continue
            current_btree = BTree(index_file_name)
            current_btree.create_index_file()
        elif command == "open":
            index_file_name = input("Enter index file name: ").strip()
            if not os.path.exists(index_file_name):
                print("Error: File not found.")
                continue
            current_btree = BTree(index_file_name)
            try:
                current_btree.load_header()
                print(f"Index file '{index_file_name}' opened successfully.")
            except ValueError as error:
                print(f"Error opening file: {error}")
                current_btree = None
        elif command == "insert":
            if not current_btree:
                print("Error: No index file is open.")
                continue
            try:
                key_to_insert = int(input("Enter key: "))
                value_to_insert = int(input("Enter value: "))
                current_btree.insert(key_to_insert, value_to_insert)
            except ValueError:
                print("Invalid input! Please enter integer values.")
        elif command == "search":
            if not current_btree:
                print("Error: No index file is open.")
                continue
            try:
                key_to_search = int(input("Enter key to search: "))
                found_value = current_btree.search(key_to_search)
                if found_value is not None:
                    print(f"Key '{key_to_search}' found with value '{found_value}'.")
                else:
                    print(f"Key '{key_to_search}' not found.")
            except ValueError:
                print("Invalid input! Please enter an integer key.")
        elif command == "load":
            if not current_btree:
                print("Error: No index file is open.")
                continue
            input_file_name = input("Enter file name containing key-value pairs: ").strip()
            if not os.path.exists(input_file_name):
                print("Error: File not found.")
                continue
            try:
                with open(input_file_name, "r") as input_file:
                    for line in input_file:
                        key, value = map(int, line.strip().split(","))
                        current_btree.insert(key, value)
                print(f"Key-value pairs successfully loaded from '{input_file_name}'.")
            except Exception as error:
                print(f"Error loading file: {error}")
        elif command == "print":
            if not current_btree:
                print("Error: No index file is open.")
                continue
            print("B-Tree contents:")
            current_btree.print_tree()
        elif command == "extract":
            if not current_btree:
                print("Error: No index file is open.")
                continue
            output_file_name = input("Enter output file name: ").strip()
            current_btree.extract_to_file(output_file_name)
        elif command == "quit":
            print("Exiting program.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
