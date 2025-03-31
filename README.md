# Daily Discovery Tracker - Documentation

## Overview
The **Daily Discovery Tracker** is a command-line application that allows users to record and retrieve their daily learnings efficiently. It provides a simple interface to add notes with topics, list saved notes, and filter them by topic. The notes are stored in a JSON file for persistence.

---

## Features
- **Add Notes**: Store a new learning with a topic and a message.
- **List Notes**: View all recorded notes.
- **Filter by Topic**: Retrieve notes related to a specific topic.
- **Exit Program**: Cleanly exit the CLI application.

---

## Installation & Setup
### Prerequisites
- Ensure you have **Python 3.x** installed on your system.

### Installation
1. Clone or download the script to your local machine.
2. No additional dependencies are required as the script uses only standard Python libraries.

---

## Usage
Run the script from the command line using:
```sh
python script.py [command] [arguments]
```

### Commands
#### 1. **Add a Note**
To add a new learning note:
```sh
python script.py add "<topic>" "<message>"
```
Example:
```sh
python script.py add "Physics" "Learned about wave functions."
```

#### 2. **List Notes**
To display all notes:
```sh
python script.py list
```
To filter notes by topic:
```sh
python script.py list --topic "<topic>"
```
Example:
```sh
python script.py list --topic "Physics"
```

#### 3. **Exit Program**
To exit the CLI tool:
```sh
python script.py exit
```

---

## Code Structure
### **1. File Handling**
- `notes.json`: Stores all notes persistently in JSON format.

### **2. Functions**
- `load()`: Loads notes from `notes.json`.
- `save(notes)`: Saves notes back to `notes.json`.
- `add(topic, message)`: Adds a new note with a timestamp.
- `list_notes(filter_topic=None)`: Lists all notes or filters them by topic.
- `exit_program()`: Exits the script.

### **3. Command Parsing**
- Uses `argparse` to handle CLI commands and arguments.
- Commands: `add`, `list`, `exit`.

---

## Example Workflow
```sh
# Adding notes
python script.py add "Math" "Understood calculus better."
python script.py add "Programming" "Explored argparse module."

# Listing notes
python script.py list

# Filtering notes by topic
python script.py list --topic "Math"

# Exiting
python script.py exit
```

---

## Notes & Improvements
- The current implementation supports basic note-taking.
- Future enhancements could include:
  - Editing or deleting notes.
  - Improving JSON storage format for efficiency.
  - Adding support for searching within messages.

---

## Author
This script was developed as a simple learning tracker using Python’s standard library.

For improvements or contributions, feel free to modify the script!

