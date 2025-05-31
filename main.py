def show_menu():
    print("\nToDoCraft")
    print("منوی اصلی")
    print("1. افزودن تسک جدید")
    print("2. نمایش تسک‌ها")
    print("3. حذف تسک")
    print("4. خروج")

def main():
    while True:
        show_menu()
        choice = input("لطفاً گزینه مورد نظر را وارد کنید: ")
        
        if choice == '1':
            print("\nافزودن تسک جدید")
            # Logic for adding a new task would go here
        elif choice == '2':
            print("\nنمایش تسک‌ها")
            # Logic for displaying tasks would go here
        elif choice == '3':
            print("\nحذف تسک")
            # Logic for deleting a task would go here
        elif choice == '4':
            print("\nخروج از برنامه\n")
            break
        else:
            print("\nگزینه نامعتبر. لطفاً عددی از 1 تا 4 وارد کنید.")
if __name__ == "__main__":
    main()