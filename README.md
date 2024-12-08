# B-Tree Index File Manager

## Overview
This project implements an interactive B-Tree index file manager. Users can create, manage, and query index files stored in a file-based structure using a B-Tree of minimal degree 10.

## Features
- Create and open index files.
- Insert key-value pairs into a B-Tree.
- Search for keys in the index file.
- Print the entire B-Tree structure.
- Extract all keys and values to a file.

## File Structure
- Each index file contains a B-Tree stored in 512-byte blocks.
- A header block stores metadata about the file.
- Nodes are dynamically allocated and written to the file.

## Commands
- `create` - Create a new index file.
- `open` - Open an existing index file.
- `insert` - Insert a key-value pair.
- `search` - Search for a key in the index.
- `print` - Print the contents of the B-Tree.
- `extract` - Save all keys and values to an external file.
- `quit` - Exit the program.

## How to Run
1. Save the code to a file named `os_p3.py`.
2. Run the program using Python:
   python3 os_p3.py
3. The in.csv file contains key-value pairs that will be loaded during the execution of the "load".
4. The out.csv file contains key-value pairs that will be extracted during the execution of the "extract".

##Example Run
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
Enter command: create       
Enter index file name: btree.idx
File exists. Overwrite? (yes/no): yes
Index file created.

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
Enter command: open  
Enter index file name: btree.idx
Index file 'btree.idx' opened successfully.

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
Enter command: insert
Enter key: 7
Enter value: 78
Inserted '78' at key '7'.

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
Enter command: insert
Enter key: 9
Enter value: 90
Inserted '90' at key '9'.

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
Enter command: load
Enter file name containing key-value pairs: in.csv
Inserted '1' at key '1'.
Inserted '2' at key '2'.
Inserted '3' at key '3'.
Inserted '4' at key '4'.
Inserted '5' at key '5'.
Inserted '6' at key '6'.
Key '7' already exists!
Inserted '8' at key '8'.
Key '9' already exists!
Inserted '10' at key '10'.
Inserted '11' at key '11'.
Inserted '12' at key '12'.
Inserted '13' at key '13'.
Inserted '14' at key '14'.
Inserted '15' at key '15'.
Key-value pairs successfully loaded from 'in.csv'.

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
Enter command: search
Enter key to search: 9
Key '9' found with value '90'.

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
Enter command: extract
Enter output file name: out.csv
File 'out.csv' exists. Overwrite? (yes/no): yes
Extracted all key-value pairs to 'out.csv'.

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
Enter command: print
B-Tree contents:
Key = '1', Value = '1'
Key = '2', Value = '2'
Key = '3', Value = '3'
Key = '4', Value = '4'
Key = '5', Value = '5'
Key = '6', Value = '6'
Key = '7', Value = '78'
Key = '8', Value = '8'
Key = '9', Value = '90'
Key = '10', Value = '10'
Key = '11', Value = '11'
Key = '12', Value = '12'
Key = '13', Value = '13'
Key = '14', Value = '14'
Key = '15', Value = '15'

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
Enter command: quit
Exiting program.
