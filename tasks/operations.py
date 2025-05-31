from datetime import datetime
from .storage import load_tasks, save_tasks
from .display import show_tasks

def add_task():
    title = input("عنوان تسک را وارد کنید: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = load_tasks()
    task.append({
        "title": title,
        "completed": False,
        "created_at": created_at
})
    save_tasks(task)
    print(f"\nتسک '{title}' با موفقیت اضافه شد.")

def edit_task():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی برای ویرایش وجود ندارد.")
        return
    show_tasks()
    while True:
        try:
            choice = int(input("\nشماره تسکی که می‌خواهید ویرایش کنید را وارد کنید: "))
            if 1 <= choice <= len(tasks):
                current_title = tasks[choice - 1]['title']
                new_title = input(f"عنوان جدید برای «{current_title}» رو وارد کنید: ").strip()
                if new_title:
                    tasks[choice - 1]['title'] = new_title
                    save_tasks(tasks)
                    print(f"\nتسک با موفقیت ویرایش شد. عنوان جدید: {new_title}")
                    break
                else:
                    print("ویرایش لغو شد. عنوان جدید نباید خالی باشد.")
            else:
                print(f"\nگزینه نامعتبر. لطفاً عددی بین 1 و {len(tasks)} وارد کنید.")
        except ValueError:
            print("\nخطا: لطفاً یک عدد صحیح وارد کنید.")
            
def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی برای حذف وجود ندارد.")
        return
    show_tasks()
    try:
        choice = int(input("\nشماره تسکی که می‌خواهید حذف کنید را وارد کنید: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"\nتسک '{removed_task['title']}' با موفقیت حذف شد.")
        else:
            print(f"\nگزینه نامعتبر. لطفاً عددی بین 1 و {len(tasks)} وارد کنید.")
    except ValueError:
        print("\nخطا: لطفاً یک عدد صحیح وارد کنید.")
        
def mark_task_completed():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی برای تیک زدن وجود ندارد.")
        return
    show_tasks()
    try:
        choice = int(input("\nشماره تسکی که انجام شده را وارد کنید: "))
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1]['completed']:
                print("\nاین تسک قبلاً انجام شده است.")
            else:
                tasks[choice - 1]['completed'] = True
                save_tasks(tasks)
                print(f"\nتسک '{tasks[choice - 1]['title']}' با موفقیت تیک زده شد.")
        else:
            print(f"\nشماره وارد شده نامعتبر است. لطفاً عددی بین 1 و {len(tasks)} وارد کنید.")
    except ValueError:
        print("\nخطا: لطفاً یک عدد صحیح وارد کنید.")
