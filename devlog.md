# Development Log

## [2024-12-08 10:00 AM]
- **Thoughts**:
  - The project involves creating and managing index files using a B-Tree structure.
  - The file structure must comply with strict specifications for headers and nodes.

- **Plan**:
  - Design and implement the basic file structure for the index file.
  - Add commands for creating and opening files.

---

## [2024-12-08 01:00 PM]
- **Thoughts**:
  - Successfully implemented the `create` and `open` commands.
  - Tested file creation and verified the header format matches specifications.

- **Plan**:
  - Add functionality for `insert` and `search` commands.
  - Ensure the B-Tree properties are maintained when inserting keys.

---

## [2024-12-08 04:00 PM]
- **Thoughts**:
  - Implemented the `insert` command to handle key-value pairs.
  - Added logic to manage the root node and maintain node structure.

- **Plan**:
  - Implement the `search` command to allow querying keys in the index file.
  - Add preliminary tests for the `insert` and `search` commands.

---

## [2024-12-09 10:00 AM]
- **Thoughts**:
  - `search` functionality added and verified for simple cases.
  - Challenges encountered in managing large B-Tree structures.

- **Plan**:
  - Test `insert` and `search` for edge cases.
  - Add the `print` and `extract` commands.

---

## [2024-12-07 09:30 PM]
- **Reflections**:
  - Completed all primary commands: `create`, `open`, `insert`, `search`, `print`, and `extract`.
  - Resolved issues with file I/O and verified correct B-Tree behavior.

- **Next Steps**:
  - Write a `README.md` file to document the project.
  - Package the repository for submission.
