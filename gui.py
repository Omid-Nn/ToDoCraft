import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("مدیریت تسک ها - ToDoCraft")
    root.geometry("800x600")
    
    title_lable = ttk.Label(root, text="به سیستم مدیریت تسک ها خوش آمدید", font=("Arial", 18))
    title_lable.pack(pady=20)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
