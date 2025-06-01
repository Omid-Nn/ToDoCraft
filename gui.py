import tkinter as tk
from tkinter import ttk, messagebox
from tasks.storage import load_tasks, save_tasks
from datetime import datetime

def open_add_task_window():
    add_win = tk.Toplevel()
    add_win.title("افزودن تسک جدید")
    add_win.geometry("400x150")

    ttk.Label(add_win, text="عنوان تسک").pack(pady=10)
    title_entry = ttk.Entry(add_win, width=50, justify="center")
    title_entry.pack()

    def save_task():
        title = title_entry.get().strip()
        if not title:
            ttk.Label(add_win, text="عنوان تسک نمی‌تواند خالی باشد", foreground="red").pack()
            return
        tasks = load_tasks()
        tasks.append({
            "title": title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_tasks(tasks)
        add_win.destroy()

    ttk.Button(add_win, text="ذخیره", command=save_task).pack(pady=20)
    add_win.bind("<Return>", lambda event=None: save_task())

def open_task_list_window():
    tasks = load_tasks()
    list_win = tk.Toplevel()
    list_win.title("لیست تسک‌ها")
    list_win.geometry("600x500")

    columns = ("created_at", "status", "title")
    tree = ttk.Treeview(list_win, columns=columns, show='headings')
    tree.heading("title", text="عنوان تسک")
    tree.heading("status", text="وضعیت")
    tree.heading("created_at", text="تاریخ ایجاد")

    tree.column("title", width=250, anchor="center")
    tree.column("status", width=50, anchor="center")
    tree.column("created_at", width=100, anchor="center")
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    def clear_selection(event):
        if not tree.identify_row(event.y):
            tree.selection_remove(tree.selection())

    tree.bind("<Button-1>", clear_selection, add="+")

    def refresh_tree():
        tasks[:] = load_tasks()
        tree.delete(*tree.get_children())
        for task in tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", values=(task['created_at'], status, task['title']))

    refresh_tree()

    button_frame = ttk.Frame(list_win)
    button_frame.pack(pady=10)

    def get_selected_index():
        selected = tree.selection()
        return tree.index(selected[0]) if selected else None

    def delete_selected_task():
        index = get_selected_index()
        if index is not None:
            if messagebox.askyesno("تایید حذف", "آیا از حذف تسک اطمینان دارید؟", parent=list_win):
                tasks.pop(index)
                save_tasks(tasks)
                refresh_tree()
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید.", parent=list_win)

    def complete_selected_task():
        index = get_selected_index()
        if index is not None:
            if not tasks[index]['completed']:
                tasks[index]['completed'] = True
                save_tasks(tasks)
                refresh_tree()
            else:
                tk.messagebox.showinfo("اطلاع", "این تسک قبلاً انجام شده است.", parent=list_win)
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید.", parent=list_win)

    def uncomplete_selected_task():
        index = get_selected_index()
        if index is not None:
            if tasks[index]['completed']:
                tasks[index]['completed'] = False
                save_tasks(tasks)
                refresh_tree()
            else:
                tk.messagebox.showinfo("اطلاع", "این تسک هنوز انجام نشده است.", parent=list_win)
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید.", parent=list_win)

    ttk.Button(button_frame, text="حذف تسک", command=delete_selected_task).grid(row=0, column=0, padx=10)
    ttk.Button(button_frame, text="تیک زدن تسک", command=complete_selected_task).grid(row=0, column=1, padx=10)
    ttk.Button(button_frame, text="بازنشانی تسک", command=uncomplete_selected_task).grid(row=0, column=2, padx=10)

def main():
    root = tk.Tk()
    root.title("مدیریت تسک ها - ToDoCraft")
    root.geometry("600x400")

    title_lable = ttk.Label(root, text="سیستم مدیریت تسک ها", font=("Arial", 18))
    title_lable.pack(pady=15)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="افزودن تسک جدید", width=25, command=open_add_task_window).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(button_frame, text="ویرایش تسک", width=25).grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(button_frame, text="نمایش تسک‌ها", width=25, command=open_task_list_window).grid(row=0, column=2, padx=10, pady=10)
    ttk.Button(button_frame, text="نمایش تسک ها با امکان فیلتر", width=25).grid(row=1, column=0, padx=10, pady=10)
    ttk.Button(button_frame, text="تیک زدن تسک (انجام شده)", width=25).grid(row=1, column=1, padx=10, pady=10)
    ttk.Button(button_frame, text="حذف تسک", width=25).grid(row=1, column=2, padx=10, pady=10)
    ttk.Button(button_frame, text="خروج", width=25, command=root.quit).grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
