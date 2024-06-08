import Student
import Teacher
import admit
import global_vars
import tkinter as tk
from tkinter import messagebox
active = global_vars.active
flag = global_vars.flag

def menu():
    while True:
        global  active,flag
        active = global_vars.active
        flag = global_vars.flag
        print("------------------")
        print("欢迎来到学生成绩管理系统")
        print('---------------------')
        now_id, now_name = active.get_info()
        print(f"欢迎你 {now_id}_{now_name}")
        print('---------------------')
        print("请在接下来的页面选择对应编号来完成你想要进行的操作")
        if flag == 1:
            Student.main()
        elif flag == 2:
            Teacher.main()
        elif flag ==9:
            admit.main()


"""def window():
    root = tk.Tk()
    root.title("页面")
    root.geometry("800x600")  # 设置窗口初始大小

    welcome_label = tk.Label(root, text="------------------\n欢迎来到学生成绩管理系统\n---------------------")
    welcome_label.pack()

    now_id, now_name = active.get_info()
    info_label = tk.Label(root, text=f"欢迎你 {now_id}_{now_name}\n---------------------")
    info_label.pack()

    instruction_label = tk.Label(root, text="请在接下来的页面选择对应编号来完成你想要进行的操作")
    instruction_label.pack()

    root.mainloop()
    return root  # 返回 root 对象"""