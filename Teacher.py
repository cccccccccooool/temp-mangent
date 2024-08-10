from usually import *
import sys
def get_buttons(root):
    actions = [
        ("更改自己的密码", lambda: change_pwd(0)),
        ("查询学生成绩", select1),
        ("录入学生成绩", insert_score),
        ("修改学生成绩", update_score),
        ("AI分析", ai),
        ("退出成绩管理系统", sys.exit),
    ]
    for (text, command) in actions:
        button = tk.Button(root, text=text, command=command)
        button.pack(pady=5)

def main():
    root = tk.Tk()
    root.title("成绩管理系统")
    root.geometry("400x400")

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
    label_frame.pack(pady=10)

    for line in text_lines:
        label = tk.Label(label_frame, text=line)
        label.pack(anchor='w')

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()