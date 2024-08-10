from SystemDriver import *
from menu import *
import global_vars
import tkinter as tk
from tkinter import messagebox

def submit(event=None):
    username = username_entry.get()
    password = password_entry.get()

    try:
        global_vars.active = STUDENTS_MANAGEMENT_SYSTEM(username, password)
        if not global_vars.login_flag:
            tk.messagebox.showerror("错误", "用户名或密码错误，请重新输入！")
            username_entry.delete(0, tk.END)  # 清空用户名输入框
            password_entry.delete(0, tk.END)  # 清空密码输入框
            return
        else:
            root.destroy()
            menu()
    except Exception as e:
        messagebox.showinfo("提示",f"{e}")
        exit()
root = tk.Tk()
root.title("登录")
root.geometry("300x150")

username_label = tk.Label(root, text="用户名")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()
username_entry.bind('<Return>', submit)

password_label = tk.Label(root, text="密码")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.bind('<Return>', submit)

login_button = tk.Button(root, text="登录", command=submit)
login_button.pack()

root.mainloop()