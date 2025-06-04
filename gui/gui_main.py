import tkinter as tk
from tkinter import ttk
from gui.gui_add import open_add_task_window
from gui.gui_list import open_task_list_window

def main():
    """
    تابع اصلی اجرای برنامه
    """
    root = tk.Tk()
    root.title("مدیریت تسک ها - ToDoCraft")
    root.geometry("500x300")

    title_lable = ttk.Label(root, text="سیستم مدیریت تسک ها", font=("Arial", 18))
    title_lable.pack(pady=15)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="افزودن تسک جدید", width=25, command=open_add_task_window).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(button_frame, text="نمایش تسک‌ها", width=25, command=open_task_list_window).grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(button_frame, text="خروج", width=25, command=root.quit).grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
