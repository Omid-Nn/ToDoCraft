# ToDoCraft

ToDoCraft is a simple and practical command-line To-Do list manager written in Python.  
It allows users to add, view, edit, complete, filter, and delete tasks. All tasks are stored in a JSON file for persistence.

---

## Features

| Feature             | Description                                  |
|---------------------|----------------------------------------------|
| Add Task            | Create a new task with a title and timestamp |
| View Tasks          | List all tasks with their status and creation time |
| Edit Task           | Modify the title of an existing task         |
| Filter Tasks        | Show only completed or incomplete tasks      |
| Complete Task       | Mark a task as completed                     |
| Delete Task         | Remove a task from the list                  |
| JSON Storage        | Tasks are saved to `tasks.json` persistently |

---

## Project Structure

```
ToDoCraft/
├── main.py                  # Entry point of the application
├── tasks/
│   ├── __init__.py         # Empty init file to define package
│   ├── storage.py          # Handles loading/saving tasks from/to JSON
│   ├── operations.py       # Task logic: add/edit/delete/complete
│   └── display.py          # Display and filter task functions
├── tasks.json              # Data file (created automatically)
```

---

## How to Run

1. Navigate to the project directory:
```bash
cd ToDoCraft
```

2. Run the application:
```bash
python main.py
```

---

## Requirements

No external dependencies are required.  
Compatible with Python **3.8+**

---

## Development Guidelines

The code is modular and easy to extend.  
You can add new features like:

- Task search
- Exporting to CSV or PDF
- GUI using tkinter or textual
- Due dates and reminders
- Cloud storage integration

---

## Security Note

The `tasks.json` file stores all user data.  
Avoid manually modifying or deleting this file to prevent data loss.

---

## Author

Developed by Omid Nourinia
Email: omid.nourinia.971202@gmail.com