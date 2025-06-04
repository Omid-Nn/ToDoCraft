"""
این فایل شامل حلقه اصلی اجرای برنامه، نمایش منو و مدیریت ورودی کاربر است.
با استفاده از ماژول‌های دیگر عملیات مربوط به تسک‌ها را اجرا می‌کند.
"""
__version__ = "1.0.0"

from cli.cli_display import show_tasks, filter_tasks
from cli.cli_operations import (
    add_task,
    edit_task,
    delete_task,
    mark_task_completed
)

def show_menu():
    """
    چاپ منوی اصلی در ترمینال برای نمایش گزینه‌های مدیریت تسک‌ها.
    """
    print(f"\nToDoCraft - نسخه {__version__}")
    print("منوی اصلی")
    print("1. افزودن تسک جدید")
    print("2. ویرایش تسک")
    print("3. نمایش تسک‌ها")
    print("4. نمایش تسک ها با امکان فیلتر")
    print("5. تیک زدن تسک (انجام شده)")    
    print("6. حذف تسک")
    print("7. خروج")

def main():
    """
    حلقه اصلی برنامه برای دریافت ورودی کاربر و اجرای عملیات انتخاب‌شده.
    در صورت وارد کردن عدد ۷، برنامه خاتمه می‌یابد.
    """
    while True:
        show_menu()
        choice = input("لطفاً گزینه مورد نظر را وارد کنید (1-7): ")

        if choice == '1':
            print("\nافزودن تسک جدید")
            add_task()

        elif choice == '2':
            edit_task()

        elif choice == '3':
            show_tasks()

        elif choice == '4':
            filter_tasks()

        elif choice == '5':
            mark_task_completed()

        elif choice == '6':
            delete_task()

        elif choice == '7':
            print("\nاز برنامه خارج شدید. بدرود\n")
            break
        else:
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 7 وارد کنید.")

if __name__ == "__main__":
    main()
