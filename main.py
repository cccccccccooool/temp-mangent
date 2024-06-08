from SystemDriver import *
from menu import *
import global_vars
import tkinter as tk
from tkinter import messagebox
admit_account = ["admit"]
#管理员默认密码为123456
#未来在这给他整个页面，开始输入一行登录密码，然后重绘页面即可

#这里改进了认证flag，直接通过学生id来认证

if __name__ == '__main__':
    username = input("请输入用户名\n")
    password = input("请输入密码\n")
    try:
        global_vars.active = STUDENTS_MANAGEMENT_SYSTEM(username, password)
        if not global_vars.active:
            messagebox.showerror("错误", "密码错误")
        else:
            menu()
    except Exception as e:
        messagebox.showerror("错误", f"Error: {e}")

"""root = tk.Tk()
root.title("登录")
root.geometry("800x600")  # 设置窗口初始大小


username_label = tk.Label(root, text="用户名")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="密码")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="提交", command=submit)
submit_button.pack()

root.mainloop()
"""