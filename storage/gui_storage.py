"""
این ماژول مسئول خواندن و نوشتن لیست تسک‌ها از/به فایل gui_tasks.json است.
"""

import json
import os

TASKS_FILE = 'gui_tasks.json'

def load_tasks():
    """
    بارگذاری تسک‌ها از فایل gui_tasks.json.

    Returns:
        list: لیستی از دیکشنری‌های تسک. اگر فایل وجود نداشته باشد، لیست خالی بازگردانده می‌شود.
    """
    try:
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                print(f"Warning: {TASKS_FILE} content is not a list. Starting with an empty tasks list.")
                return []
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {TASKS_FILE} is crorpted or invalid. Starting with an empty tasks list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading tasks: {e}. Starting with an empty tasks list.")
        return []

def save_tasks(tasks):
    """
    ذخیره لیست تسک‌ها در فایل gui_tasks.json.

    Args:
        tasks (list): لیست تسک‌هایی که باید ذخیره شوند.
    """
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)