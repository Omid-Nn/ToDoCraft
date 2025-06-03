import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import uuid
from tasks.storage import load_tasks, save_tasks

def normalize_persian(text):
    return text.strip().replace('ي', 'ی').replace('ك', 'ک').replace('‌', ' ').lower()

def open_add_task_window(refresh_callback=None):
    add_win = tk.Toplevel()
    add_win.title("افزودن تسک جدید")
    add_win.geometry("400x150")

    ttk.Label(add_win, text="عنوان تسک").pack(pady=10)
    title_entry = ttk.Entry(add_win, width=50, justify="center")
    title_entry.pack()
    
    error_label = ttk.Label(add_win, text="", foreground="red")
    error_label.pack()
    
    def save_task():
        title = title_entry.get().strip()
        if not title:
            error_label.config(text="عنوان تسک نمی‌تواند خالی باشد")
            return
        tasks = load_tasks()

        normalized_title = normalize_persian(title)
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

        tasks.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_tasks(tasks)
        add_win.destroy()

        if refresh_callback:
            refresh_callback()
        
    ttk.Button(add_win, text="ذخیره", command=save_task).pack(pady=20)
    add_win.bind("<Return>", lambda event=None: save_task())
    title_entry.focus_set()

def open_task_list_window():
    tasks = load_tasks()
    list_win = tk.Toplevel()
    list_win.title("لیست تسک‌ها")
    list_win.geometry("600x500")

    columns = ("created_at", "status", "title")
    tree = ttk.Treeview(list_win, columns=columns, show='headings')

    tree.column("#0", width=0, stretch=tk.NO)

    sort_order = {"title": False, "status": False, "created_at": False}

    current_sort_col = tk.StringVar(value="")
    current_sort_reverse = tk.BooleanVar(value=False)

    tree.heading("title", text="عنوان تسک", command=lambda: sort_column("title"))
    tree.heading("status", text="وضعیت", command=lambda: sort_column("status"))
    tree.heading("created_at", text="تاریخ ایجاد", command=lambda: sort_column("created_at"))

    tree.column("title", width=250, anchor="center")
    tree.column("status", width=50, anchor="center")
    tree.column("created_at", width=100, anchor="center")

    search_frame = ttk.Frame(list_win)
    search_frame.pack(pady=5)

    ttk.Label(search_frame, text="جستجو براساس عنوان").pack(side='right')
    search_entry = ttk.Entry(search_frame, width=30, justify="center")
    search_entry.pack(side='right', padx=5)

    def search_tasks():
        keyword = normalize_persian(search_entry.get())
        tree.delete(*tree.get_children())

        filtered_tasks = [task for task in tasks if keyword in normalize_persian(task['title'])]

        col_to_sort = current_sort_col.get()
        reverse_sort = current_sort_reverse.get()

        if col_to_sort:
            filtered_tasks = sorted(filtered_tasks, key=lambda x: x[col_to_sort] if col_to_sort != "status" else not x['completed'], reverse=reverse_sort)

        for task in filtered_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

    list_win.bind("<Return>", lambda event=None: search_tasks())

    def refresh_tree():
        tasks[:] = load_tasks()
        tree.delete(*tree.get_children())

        col_to_sort = current_sort_col.get()
        reverse_sort = current_sort_reverse.get()

        display_tasks = tasks

        if col_to_sort:
            display_tasks = sorted(tasks, key=lambda x: x[col_to_sort] if col_to_sort != "status" else not x['completed'], reverse=reverse_sort)

        for task in display_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

        search_entry.delete(0, tk.END)

    ttk.Button(search_frame, text=" جستجو", command=search_tasks).pack(side="left")
    ttk.Button(search_frame, text="نمایش همه", command=refresh_tree).pack(side="left", padx=5)

    tree.pack(expand=True, fill='both', padx=10, pady=(5, 0))

    vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    def clear_selection(event):
        if not tree.identify_row(event.y):
            tree.selection_remove(tree.selection())

    tree.bind("<Button-1>", clear_selection, add="+")

    refresh_tree()

    def sort_column(col):
        reverse = not sort_order[col]
        sort_order[col] = reverse

        current_sort_col.set(col)
        current_sort_reverse.set(reverse)

        sorted_tasks = sorted(tasks, key=lambda x: x[col] if col != "status" else not x['completed'], reverse=reverse)

        tree.delete(*tree.get_children())

        for task in sorted_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

    button_frame = ttk.Frame(list_win)
    button_frame.pack(pady=10)

    def get_selected_id():
        selected = tree.selection()
        if not selected:
            return None
        selected_id = tree.focus()
        return selected_id

    def delete_selected_task():
        selected_id = get_selected_id()
        if selected_id:
            if messagebox.askyesno("تایید حذف", "آیا از حذف تسک اطمینان دارید؟", parent=list_win):
                current_tasks = load_tasks()

                updated_tasks = [task for task in current_tasks if task.get('id') != selected_id]

                if len(updated_tasks) < len(current_tasks):
                    save_tasks(updated_tasks)
                    refresh_tree()
                else:
                    tk.messagebox.showwarning("خطا", "تسک انتخاب شده یافت نشد.", parent=list_win)
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید.", parent=list_win)

    def complete_selected_task():
        selected_id = get_selected_id()
        if selected_id:
            current_tasks = load_tasks()
            found = False
            for task in current_tasks:
                if task.get('id') == selected_id:
                    if not task['completed']:
                        task['completed'] = True
                        found = True
                        break
                    tk.messagebox.showinfo("اطلاع", "این تسک قبلاً انجام شده است", parent=list_win)
                    return

            if found:
                save_tasks(current_tasks)
                refresh_tree()
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید", parent=list_win)

    def uncomplete_selected_task():
        selected_id = get_selected_id()
        if selected_id:
            current_tasks = load_tasks()
            found = False
            for task in current_tasks:
                if task.get('id') == selected_id:
                    if task['completed']:
                        task['completed'] = False
                        found = True
                        break

                    tk.messagebox.showinfo("اطلاع", "این تسک هنوز انجام نشده است.", parent=list_win)
                    return

            if found:
                save_tasks(current_tasks)
                refresh_tree()
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید.", parent=list_win)

    def edit_selected_task():
        selected_id = get_selected_id()
        if selected_id:
            current_tasks = load_tasks()
            task_to_edit = None
            for task in current_tasks:
                if task.get('id') == selected_id:
                    task_to_edit = task
                    break
            
            if task_to_edit:
                edit_win = tk.Toplevel(list_win)
                edit_win.title("ویرایش تسک")
                edit_win.geometry("400x150")
                
                ttk.Label(edit_win, text="عنوان تسک جدید").pack(pady=10)
                new_title_entry = ttk.Entry(edit_win, width=50, justify="center")
                new_title_entry.insert(0, task_to_edit['title'])
                new_title_entry.pack()
            
                def save_edit():
                    new_title = new_title_entry.get().strip()
                    if not new_title:
                        messagebox.showwarning("هشدار", "عنوان تسک نمی‌تواند خالی باشد", parent=edit_win)
                        return
                    task_to_edit['title'] = new_title
                    save_tasks(current_tasks)
                    refresh_tree()
                    edit_win.destroy()
                ttk.Button(edit_win, text="ذخیره", command=save_edit).pack(pady=15)
                edit_win.bind("<Return>", lambda event=None: save_edit())
                new_title_entry.focus_set()
            else:
                tk.messagebox.showwarning("خطا", "تسک انتخاب شده یافت نشد.", parent=list_win)
        else:
            tk.messagebox.showwarning("هشدار", "لطفاً یک تسک انتخاب کنید", parent=list_win)

    ttk.Button(button_frame, text="حذف تسک", command=delete_selected_task).grid(row=0, column=0, padx=10)
    ttk.Button(button_frame, text="بازنشانی تسک", command=uncomplete_selected_task).grid(row=0, column=1, padx=10)
    ttk.Button(button_frame, text="تیک زدن تسک", command=complete_selected_task).grid(row=0, column=2, padx=10)
    ttk.Button(button_frame, text="ویرایش تسک", command=edit_selected_task).grid(row=0, column=3, padx=10)
    ttk.Button(button_frame, text="افزودن تسک جدید", command=lambda: open_add_task_window(refresh_tree)).grid(row=0, column=4, padx=10)

def main():
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
