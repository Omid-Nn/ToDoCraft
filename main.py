import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

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

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی وجود ندارد.")
        return

    print("\nلیست تسک‌ها:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{index}. {task['title']} [{status}] - {task['created_at']}")

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

def filter_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی وجود ندارد.")
        return
    
    while True:
        print("\n1. نمایش همه تسک‌ها")
        print("2. نمایش تسک‌های انجام نشده")
        print("3. نمایش تسک‌های انجام شده")
        print("4. بازگشت به منوی اصلی")
        choice = input("لطفاً گزینه مورد نظر را برای مرتب سازی وارد کنید (1-6): ")
        if choice not in list(range(1, 5)):
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 4 وارد کنید.")
        else:
            print("\nلیست تسک‌ها:")

            for index, task in enumerate(tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                if choice == '1':
                    print(f"{index}. {task['title']} [{status}] - {task['created_at']}")
                elif choice == '2' and not task['completed']:
                    print(f"{index}. {task['title']} [{status}] - {task['created_at']}")
                elif choice == '3' and task['completed']:
                    print(f"{index}. {task['title']} [{status}] - {task['created_at']}")
                elif choice == '4':
                    return


def show_menu():
    print("\nToDoCraft")
    print("منوی اصلی")
    print("1. افزودن تسک جدید")
    print("2. نمایش تسک‌ها")
    print("3. نمایش تسک ها با امکان فیلتر")
    print("4. حذف تسک")
    print("5. تیک زدن تسک (انجام شده)")
    print("6. خروج")

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

def main():
    while True:
        show_menu()
        choice = input("لطفاً گزینه مورد نظر را وارد کنید (1-6): ")

        if choice == '1':
            print("\nافزودن تسک جدید")
            add_task()

        elif choice == '2':
            show_tasks()

        elif choice == '3':
            filter_tasks()

        elif choice == '4':
            delete_task()

        elif choice == '5':
            mark_task_completed()

        elif choice == '6':
            print("\nاز برنامه خارج شدید. بدرود\n")
            break
        else:
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 6 وارد کنید.")

if __name__ == "__main__":
    main()
