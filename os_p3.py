import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4337PRJ3"

class BTree:
    def __init__(self):
        self.file_path = None
        self.root_block_id = 0
        self.next_block_id = 1

    def create(self):
        file_path = input("Enter file name to create: ").strip()
        if os.path.exists(file_path):
            overwrite = input("File exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != "yes":
                print("Aborted.")
                return
        with open(file_path, "wb") as f:
            # Write header block
            header = MAGIC_NUMBER + (0).to_bytes(8, 'big') + (1).to_bytes(8, 'big')
            header = header.ljust(BLOCK_SIZE, b'\x00')
            f.write(header)
        self.file_path = file_path
        self.root_block_id = 0
        self.next_block_id = 1
        print(f"File '{file_path}' created and opened.")

    def menu(self):
        while True:
            print("\nCommands: create, quit")
            command = input("Enter a command: ").strip().lower()
            if command == "create":
                self.create()
            elif command == "quit":
                print("Exiting.")
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    tree = BTree()
    tree.menu()
