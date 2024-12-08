# B-Tree Index File Manager

## Overview
This project implements an interactive B-Tree index file manager. Users can create, manage, and query index files stored in a file-based structure using a B-Tree of minimal degree 10.

I was travelling duirng the duration of this project, hence all the commits were made late.


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
   python3 btree.py
