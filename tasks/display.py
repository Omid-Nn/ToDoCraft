from .storage import load_tasks

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nهیچ تسکی وجود ندارد.")
        return

    print("\nلیست تسک‌ها:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{index}. {task['title']} [{status}] - {task['created_at']}")



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
        choice = input("لطفاً گزینه مورد نظر را برای مرتب سازی وارد کنید (1-4): ")
        if choice not in ['1', '2', '3', '4']:
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 4 وارد کنید.")
        elif choice ==  '4':
            return
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
