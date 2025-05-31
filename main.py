import json
import os

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
    task = load_tasks()
    task.append({"title": title, "completed": False})
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
        print(f"{index}. {task['title']} [{status}]")

def show_menu():
    print("\nToDoCraft")
    print("منوی اصلی")
    print("1. افزودن تسک جدید")
    print("2. نمایش تسک‌ها")
    print("3. حذف تسک")
    print("4. خروج")

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
            print(f"\nشماره وارد شده نامعتبر است. لطفاً عددی بین 1 و {format(len(tasks))} وارد کنید.")
    except ValueError:
        print("\nخطا: لطفاً یک عدد صحیح وارد کنید.")

def main():
    while True:
        show_menu()
        choice = input("لطفاً گزینه مورد نظر را وارد کنید (1-4): ")

        if choice == '1':
            print("\nافزودن تسک جدید")
            add_task()
        elif choice == '2':
            show_tasks()

        elif choice == '3':
            delete_task()

        elif choice == '4':
            print("\nخروج از برنامه\n")
            break
        else:
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 4 وارد کنید.")
if __name__ == "__main__":
    main()
