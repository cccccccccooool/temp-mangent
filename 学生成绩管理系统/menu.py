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
        print("------------------------------------------")
        print("\t欢迎来到学生成绩管理系统\t\t\t")
        print('------------------------------------------')
        now_id, now_name = active.get_info()
        print(f"\t欢迎您 {now_id}_{now_name}\t\t\t")
        print('------------------------------------------')
        print("请在接下来的页面选择对应编号来完成你想要进行的操作")
        if flag == 1:
            Student.main()
        elif flag == 2:
            Teacher.main()
        elif flag ==9:
            admit.main()
