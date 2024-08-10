import sys
from tkinter import messagebox
from usually import *
import global_vars
import tkinter as tk

def change_info(temp_flag):
    # 懒得做合理性检测了，凡是主键id都不允许被修改
    active = global_vars.active
    root = tk.Tk()
    root.withdraw()
    change_type = int(simpledialog.askstring("输入", "当前仅支持修改\t1.名字和\t2.班别/授课科目\t请选择一项目", parent=root))
    if change_type is None:
        return
    if change_type not in [1, 2]:
        if error_1():
            return
        else:
            return change_info(temp_flag)
    changed_id = simpledialog.askstring("输入", "请输入要被更改的人的id", parent=root)
    if changed_id is None:
        return
    try:
        if change_type == 1:
            if temp_flag:
                temp_flag=active.change_tec_name_info(changed_id)
            else:
                temp_flag=active.change_stu_name_info(changed_id)
        else:
            if temp_flag:
                temp_flag=active.change_deep_info(changed_id)
            else:
                temp_flag=active.change_class_info(changed_id)
        if temp_flag:
            messagebox.showinfo("通知", "修改成功")
        else:
            messagebox.showinfo("通知", "取消修改")
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            change_info(temp_flag)


def add_info(teamFlag):
    active = global_vars.active
    try:
        if not teamFlag:
            stu_id=int(simpledialog.askstring("输入","请输入学生id"))
            if stu_id is None:
                return
            stu_name=simpledialog.askstring("输入","请输入姓名")
            if stu_name is None:
                return
            stu_class=simpledialog.askstring("输入","请输入班级")
            if stu_class is None:
                return
            active.add_stu_info(stu_id,stu_name,stu_class)
        else:
            tec_id = int(simpledialog.askstring("输入","请输入教师id"))
            if tec_id is None:
                return
            tec_name = simpledialog.askstring("输入","请输入姓名")
            if tec_name is None:
                return
            tec_deep = simpledialog.askstring("输入","请输入授课科目")
            if tec_deep is None:
                return
            active.add_tec_info(tec_id, tec_name, tec_deep)
        messagebox.showinfo("通知", "录入成功")
    except:
        if error_1():
            return
        else:
            add_info(teamFlag)

def delete_info(teamFlag):
    active = global_vars.active
    temp_flag=False
    try:
        if teamFlag=='1':
            if active.del_tec_info():
                temp_flag=True
        else:
            if active.del_stu_info():
                temp_flag=True
        if temp_flag:
            messagebox.showinfo("通知", "删除成功")
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            delete_info(teamFlag)

def add_lesson_info():
    active = global_vars.active
    try:
        if active.add_lesson():
            messagebox.showinfo("通知", "录入成功")
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            add_lesson_info()

def delete_lesson_info():
    active = global_vars.active
    try:
        if active.del_lesson():
            messagebox.showinfo("通知", "删除成功")
    except:
        if error_1():
            return
        else:
            delete_lesson_info()

def change_lesson_info():
    active = global_vars.active
    try:
        if active.change_lesson():
            messagebox.showinfo("通知", "修改成功")
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            change_lesson_info()



def append_username():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    add_id = simpledialog.askstring("输入", "请输入要添加的id", parent=root)
    if add_id is None:
        root.destroy()
        return
    username = simpledialog.askstring("输入", "请输入用户名", parent=root)
    if username is None:
        root.destroy()
        return
    pwd = simpledialog.askstring("输入", "请输入密码", parent=root)
    if pwd is None:
        root.destroy()
        return

    active = global_vars.active
    if active.add_account(add_id, username, pwd):
        messagebox.showinfo("通知", "录入成功")
        return
    else:
        tk.messagebox.showerror("错误", "系统出错")
        if error_1():
            return
        else:
            return append_username()

def get_all_lesson(type):
    active=global_vars.active
    active.get_all_lesson_student_teacher(type)
    return

def get_buttons(root):
    actions = [
        ("添加登录账号", append_username),
        ("查询学生成绩", select1),
        ("录入学生成绩", insert_score),
        ("修改学生成绩", update_score),
        ("编辑学生信息", lambda: change_info(0)),
        ("编辑教师信息", lambda: change_info(1)),
        ("添加学生信息", lambda: add_info(0)),
        ("添加教师信息", lambda: add_info(1)),
        ("删除学生信息", lambda: delete_info(0)),
        ("删除教师信息", lambda: delete_info(1)),
        ("查看所有学生信息", lambda: get_all_lesson(1)),
        ("查看所有教师信息", lambda: get_all_lesson(2)),
        ("修改其他成员密码", lambda: change_pwd(1)),
        ("录入课程信息", add_lesson_info),
        ("修改课程信息", change_lesson_info),
        ("删除课程信息", delete_lesson_info),
        ("查看所有课程信息", lambda: get_all_lesson(0)),
        ("退出成绩管理系统", sys.exit),
    ]
    for index, (text, command) in enumerate(actions):
        button = tk.Button(root, text=text, command=command)
        button.grid(row=index // 5, column=index % 5, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.title("成绩管理系统")
    root.geometry("600x300")

    get_buttons(root)
    active=global_vars.active
    name,id=active.get_info()
    text_lines = [
        f"{name}_{id}",
        "欢迎使用成绩管理系统。",
        "请根据需要点击相应的按钮进行操作。",
        "如有问题，请联系管理员。"
    ]

    label_frame = tk.Frame(root)
    label_frame.grid(row=(15// 4) + 1, column=0, columnspan=4, pady=10)

    for line in text_lines:
        label = tk.Label(label_frame, text=line)
        label.pack(anchor='w')

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()
