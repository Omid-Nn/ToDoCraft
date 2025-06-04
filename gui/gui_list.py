import tkinter as tk
from tkinter import ttk, messagebox
from storage.gui_storage import load_tasks, save_tasks
from gui.gui_add import open_add_task_window
from gui.gui_utils import normalize_persian

def open_task_list_window():
    """
    پنجره‌ای که لیست تسک‌ها را نمایش داده و امکان جستجو، ویرایش، حذف و تغییر وضعیت را فراهم می‌کند
    """
    tasks = load_tasks()

    list_win = tk.Toplevel()
    list_win.title("لیست تسک‌ها")
    list_win.geometry("600x500")

    # تعریف ستون‌های درخت
    columns = ("created_at", "status", "title")
    tree = ttk.Treeview(list_win, columns=columns, show='headings')
    tree.column("#0", width=0, stretch=tk.NO)

    # نگهداری وضعیت مرتب‌سازی هر ستون
    sort_order = {"title": False, "status": False, "created_at": False}
    current_sort_col = tk.StringVar(value="")
    current_sort_reverse = tk.BooleanVar(value=False)

    # تنظیم هدر ستون‌ها با قابلیت کلیک برای مرتب‌سازی
    tree.heading("title", text="عنوان تسک", command=lambda: sort_column("title"))
    tree.heading("status", text="وضعیت", command=lambda: sort_column("status"))
    tree.heading("created_at", text="زمان ایجاد", command=lambda: sort_column("created_at"))

    tree.column("title", width=250, anchor="center")
    tree.column("status", width=50, anchor="center")
    tree.column("created_at", width=100, anchor="center")

    # بخش جستجو
    search_frame = ttk.Frame(list_win)
    search_frame.pack(pady=5)

    ttk.Label(search_frame, text="جستجو براساس عنوان").pack(side='right')

    search_entry = ttk.Entry(search_frame, width=30, justify="center")
    search_entry.pack(side='right', padx=5)

    def search_tasks():
        """
        جستجو در لیست تسک‌ها با فیلتر کردن بر اساس عنوان و مرتب‌سازی بر اساس ستون فعلی
        """
        keyword = normalize_persian(search_entry.get())
        tree.delete(*tree.get_children())

        filtered_tasks = [task for task in tasks if keyword in normalize_persian(task['title'])]

        col_to_sort = current_sort_col.get()
        reverse_sort = current_sort_reverse.get()

        if col_to_sort:
            filtered_tasks = sorted(
                filtered_tasks,
                key=lambda x: x[col_to_sort] if col_to_sort != "status" else not x['completed'],
                reverse=reverse_sort
            )

        for task in filtered_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

    # اجرای جستجو با زدن Enter
    list_win.bind("<Return>", lambda event=None: search_tasks())

    def refresh_tree():
        """
        بارگذاری مجدد لیست تسک‌ها و نمایش آن در درخت، با توجه به ستون مرتب‌سازی فعلی
        """
        tasks[:] = load_tasks()
        tree.delete(*tree.get_children())

        col_to_sort = current_sort_col.get()
        reverse_sort = current_sort_reverse.get()

        display_tasks = tasks

        if col_to_sort:
            display_tasks = sorted(
                tasks,
                key=lambda x: x[col_to_sort] if col_to_sort != "status" else not x['completed'],
                reverse=reverse_sort
            )

        for task in display_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

        search_entry.delete(0, tk.END)

    # دکمه‌های جستجو و نمایش همه
    ttk.Button(search_frame, text=" جستجو", command=search_tasks).pack(side="left")
    ttk.Button(search_frame, text="نمایش همه", command=refresh_tree).pack(side="left", padx=5)

    tree.pack(expand=True, fill='both', padx=10, pady=(5, 0))

    # اسکرول بار عمودی
    vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    def clear_selection(event):
        """
        پاک کردن انتخاب در صورت کلیک خارج از ردیف‌ها 
        """
        if not tree.identify_row(event.y):
            tree.selection_remove(tree.selection())

    tree.bind("<Button-1>", clear_selection, add="+")

    refresh_tree()

    def sort_column(col):
        """
        مرتب‌سازی ستون درخت بر اساس کلیک روی هدر
        """
        reverse = not sort_order[col]
        sort_order[col] = reverse

        current_sort_col.set(col)
        current_sort_reverse.set(reverse)

        sorted_tasks = sorted(
            tasks, key=lambda x: x[col] if col != "status" else not x['completed'],
            reverse=reverse
        )

        tree.delete(*tree.get_children())

        for task in sorted_tasks:
            status = "✅" if task['completed'] else "⏳"
            tree.insert("", "end", iid=task['id'], values=(task['created_at'], status, task['title']))

    # دکمه‌ها و عملیات روی تسک انتخاب شده
    button_frame = ttk.Frame(list_win)
    button_frame.pack(pady=10)

    def get_selected_id():
        """
        دریافت شناسه تسک انتخاب شده از درخت
        """
        selected = tree.selection()
        if not selected:
            return None
        selected_id = tree.focus()
        return selected_id

    def delete_selected_task():
        """
        حذف تسک انتخاب شده با تایید کاربر
        """
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
        """
        تیک زدن تسک انتخاب شده و تغییر وضعیت آن به انجام شده
        """
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
        """
        بازنشانی وضعیت تسک انتخاب شده به انجام نشده
        """
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
        """
        ویرایش عنوان تسک انتخاب شده
        """
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

    # دکمه‌های عملیاتی
    ttk.Button(button_frame, text="حذف تسک", command=delete_selected_task).grid(row=0, column=0, padx=10)
    ttk.Button(button_frame, text="بازنشانی تسک", command=uncomplete_selected_task).grid(row=0, column=1, padx=10)
    ttk.Button(button_frame, text="تیک زدن تسک", command=complete_selected_task).grid(row=0, column=2, padx=10)
    ttk.Button(button_frame, text="ویرایش تسک", command=edit_selected_task).grid(row=0, column=3, padx=10)
    ttk.Button(button_frame, text="افزودن تسک جدید", command=lambda: open_add_task_window(refresh_tree)).grid(row=0, column=4, padx=10)
