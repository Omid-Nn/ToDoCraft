"""
این ماژول مسئول خواندن و نوشتن لیست تسک‌ها از/به فایل tasks.json است.
"""

import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    بارگذاری تسک‌ها از فایل tasks.json.

    Returns:
        list: لیستی از دیکشنری‌های تسک. اگر فایل وجود نداشته باشد، لیست خالی بازگردانده می‌شود.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_tasks(tasks):
    """
    ذخیره لیست تسک‌ها در فایل tasks.json.

    Args:
        tasks (list): لیست تسک‌هایی که باید ذخیره شوند.
    """
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
