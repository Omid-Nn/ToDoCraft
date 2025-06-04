# ToDoCraft

ToDoCraft is a modular and user-friendly To-Do list manager written in Python.  
It offers both **Command-Line Interface (CLI)** and **Graphical User Interface (GUI)** built with `tkinter`.

Users can add, view, edit, search, filter, complete, and delete tasks.    
All tasks are stored persistently in JSON files, separately for CLI and GUI modes.

---

## Features

| Feature             | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| Add Task            | Create a new task with a title and timestamp                      |
| View Tasks          | List all tasks with their status and creation time                |
| Edit Task           | Modify the title of an existing task                              |
| Search Task         | Find tasks by matching keywords in their titles 
| Filter Tasks        | Show only completed or incomplete tasks                           |
| Complete Task       | Mark a task as completed                                          |
| Delete Task         | Remove a task from the list                                       |
| GUI Mode            | Interact with tasks via a graphical interface (tkinter)           |
| CLI Mode            | Use the terminal to manage tasks                                  |
| JSON Storage        | CLI and GUI use separate JSON files (`cli_tasks.json`, `gui_tasks.json`) |

---

## Project Structure

```
ToDoCraft/
ToDoCraft/
├── cli/                                # Modules for the Command-Line Interface (CLI) version
│   ├── __init__.py                     # Package initialization file
│   ├── cli_display.py                  # Functions for displaying and filtering tasks for CLI
│   ├── cli_main.py                     # Main entry point for the CLI version
│   └── cli_operations.py               # Task operation logic for CLI (add, edit, delete, complete)
├── gui/                                # Modules for the Graphical User Interface (GUI) version
│   ├── __init__.py                     # Package initialization file
│   ├── gui_add.py                      # Logic for adding tasks in GUI
│   ├── gui_list.py                     # Logic for displaying and managing the task list in GUI
│   ├── gui_main.py                     # Main entry point for the GUI version
│   └── gui_utils.py                    # Utility functions for GUI (Persian normalization)
├── storage/                            # Modules for data storage management
│   ├── __init__.py                     # Package initialization file
│   ├── cli_storage.py                  # Load/save functions for CLI data (cli_tasks.json)
│   └── gui_storage.py                  # Load/save functions for GUI data (gui_tasks.json)
├── venv/                               # Python virtual environment folder (recommended, ignored by Git)
├── .gitignore                          # Specifies intentionally untracked files to ignore
├── cli_tasks.json                      # JSON file for storing CLI tasks data (auto-generated)
├── gui_tasks.json                      # JSON file for storing GUI tasks data (auto-generated)
├── README_PER.md                       # README file in Persian
├── README.md                           # README file in English
└── requirements.txt                    # List of required Python libraries for the project
```

---

## How to Run

### CLI Mode:

```bash
cd ToDoCraft
python -m cli.cli_main
```

### GUI Mode:

```bash
cd ToDoCraft
python -m gui.gui_main
```

---

## Requirements

- Python **3.8+**
- Required libraries:
jalali_core==1.0.0,
jdatetime==5.2.0

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Possible Future Features

- Task reminders
- Build an installable version (e.g. using PyInstaller)

---

## Security Note

Each mode (CLI / GUI) stores data in separate JSON files.  
Avoid editing them manually to prevent data corruption.

---

## Author

Developed with by **Omid Nourinia**  
Email: omid.nourinia.971202@gmail.com
