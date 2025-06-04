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
├── tasks/
│ ├── init.py # Empty file to declare package
│ ├── cli_storage.py # CLI-specific task storage
│ ├── gui_storage.py # GUI-specific task storage
│ ├── display.py # Task display and filter functions
│ └── operations.py # Core logic for task operations
├── cli_tasks.json # Data file for CLI mode
├── gui_tasks.json # Data file for GUI mode
├── gui.py # GUI application using tkinter
├── main.py # CLI application entry point
├── requirements.txt # List of dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore file
```

---

## How to Run

### CLI Mode:

```bash
cd ToDoCraft
python main.py
```

### GUI Mode:

```bash
cd ToDoCraft
python gui.py
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
