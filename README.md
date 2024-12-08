# B-Tree Index File Manager

## Overview
The B-Tree Index File Manager is an interactive Python-based program that enables users to create, manage, and query index files stored in a file-based structure using a B-Tree with a minimal degree of 10.

## Features

### Core Functionalities:
1. **Create and Open Index Files**  
   - Create new index files to store key-value pairs.
   - Open and manage existing index files.

2. **Insert Key-Value Pairs**  
   - Add new key-value pairs to the B-Tree.
   - Handles duplicate key insertion gracefully.

3. **Search for Keys**  
   - Quickly retrieve the value associated with a given key.

4. **Print B-Tree Structure**  
   - Display all key-value pairs stored in the B-Tree.

5. **Load Key-Value Pairs from File**  
   - Load key-value pairs from a CSV file for batch insertion.

6. **Extract Data to File**  
   - Export all key-value pairs in the B-Tree to a CSV file.

7. **Quit Program**  
   - Safely exit the program.

---

## File Structure

- **Index File**:  
  Each index file is structured using 512-byte blocks:
  - **Header Block**: Contains metadata (e.g., B-Tree degree, file size, root node location).
  - **Node Blocks**: Dynamically allocated to store B-Tree nodes.

- **External Files**:
  - `in.csv`: Input file containing key-value pairs to be loaded.
  - `out.csv`: Output file for extracted key-value pairs.

---

## Commands

| Command   | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| `create`  | Create a new index file.                                                                        |
| `open`    | Open an existing index file.                                                                    |
| `insert`  | Insert a single key-value pair into the B-Tree.                                                 |
| `search`  | Search for a specific key and retrieve its associated value.                                    |
| `load`    | Load multiple key-value pairs from a CSV file (`in.csv`).                                       |
| `print`   | Print the entire B-Tree structure to the console.                                               |
| `extract` | Export all key-value pairs in the B-Tree to a CSV file (`out.csv`).                             |
| `quit`    | Exit the program.                                                                               |

---

## How to Run

1. **Save the script**  
   Save the program code to a file named `os_p3.py`.

2. **Run the program**  
   Execute the program using Python 3:
   ```bash
   python3 os_p3.py
   ```

3. **Follow the command menu**  
   Use the interactive command menu to perform various operations.

---

## Example Run

### Command Menu:
```plaintext
========================================
            COMMAND MENU
========================================
  create  - Create a new index file
  open    - Open an existing index file
  insert  - Insert a key-value pair
  search  - Search for a key
  load    - Load key-value pairs from a file
  print   - Print B-Tree structure
  extract - Save keys and values to a file
  quit    - Exit the program
========================================
```

### Example Workflow:
1. Create a new index file:
   ```plaintext
   Enter command: create
   Enter index file name: btree.idx
   File exists. Overwrite? (yes/no): yes
   Index file created.
   ```

2. Insert a key-value pair:
   ```plaintext
   Enter command: insert
   Enter key: 7
   Enter value: 78
   Inserted '78' at key '7'.
   ```

3. Search for a key:
   ```plaintext
   Enter command: search
   Enter key to search: 7
   Key '7' found with value '78'.
   ```

4. Print the B-Tree:
   ```plaintext
   Enter command: print
   B-Tree contents:
   Key = '7', Value = '78'
   ```

5. Export data to a file:
   ```plaintext
   Enter command: extract
   Enter output file name: out.csv
   File 'out.csv' exists. Overwrite? (yes/no): yes
   Extracted all key-value pairs to 'out.csv'.
   ```

6. Quit the program:
   ```plaintext
   Enter command: quit
   Exiting program.
   ```

---

## Input/Output Files

- **`in.csv`**  
  Contains key-value pairs for batch loading (e.g., during the `load` command).

  Example:
  ```csv
  1,One
  2,Two
  3,Three
  ```

- **`out.csv`**  
  Stores extracted key-value pairs from the B-Tree (e.g., during the `extract` command).

---

## Notes

- Keys must be unique. Attempting to insert a duplicate key will be rejected.
- The B-Tree is implemented with a minimum degree of 10 for optimal performance.
- File operations are designed to handle dynamic memory allocation and ensure data integrity.

---

## Dependencies

- Python 3.x
- CSV files (`in.csv`, `out.csv`) for data input/output
