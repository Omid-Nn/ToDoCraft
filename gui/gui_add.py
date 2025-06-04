import tkinter as tk
from tkinter import ttk, messagebox
import uuid
import jdatetime
from storage.gui_storage import load_tasks, save_tasks
from gui.gui_utils import normalize_persian

def open_add_task_window(refresh_callback=None):
    """
    پنجره افزودن تسک جدید با اعتبارسنجی عنوان و جلوگیری از تکراری بودن
    """
    add_win = tk.Toplevel()
    add_win.title("افزودن تسک جدید")
    add_win.geometry("400x150")

    ttk.Label(add_win, text="عنوان تسک").pack(pady=10)
    title_entry = ttk.Entry(add_win, width=50, justify="center")
    title_entry.pack()

    error_label = ttk.Label(add_win, text="", foreground="red")
    error_label.pack()

    def save_task():
        """
        ذخیره تسک جدید با امکان سنجش عنوان تکراری و گرفتن تایید از کاربر
        """
        title = title_entry.get().strip()
        if not title:
            error_label.config(text="عنوان تسک نمی‌تواند خالی باشد")
            return
        tasks = load_tasks()

        normalized_title = normalize_persian(title)

        # چک کردن تکراری بودن عنوان
        for task in tasks:
            existing_title = normalize_persian(task['title'])
            if normalized_title == existing_title:
                answer = messagebox.askyesno(
                    "تسک تکراری",
                    "این تسک قبلاً وجود دارد. آیا می‌خواهید آن را دوباره اضافه کنید؟",
                    parent=add_win
                )
                if not answer:
                    return
                break

        # اضافه کردن تسک جدید
        tasks.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "completed": False,
            "created_at": jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_tasks(tasks)
        add_win.destroy()

        if refresh_callback:
            refresh_callback()

    ttk.Button(add_win, text="ذخیره", command=save_task).pack(pady=20)
    add_win.bind("<Return>", lambda event=None: save_task())
    title_entry.focus_set()
