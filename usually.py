import hashlib
from tkinter import simpledialog, messagebox,scrolledtext
import requests
import global_vars
from pypinyin import lazy_pinyin
import tkinter as tk


# 报错统一模板
def error_1():
    get = simpledialog.askstring("输入","输入有误，请重新输入,输入任意继续,输入0或点击右下角则退出当前模式\n")
    if get is None:
        return True
    if get == "0":
        return True
    return False


# hash加密
def hash_password(password):
    # 创建一个新的哈希对象
    sha256 = hashlib.sha256()
    # 使用给定的密码更新哈希对象
    sha256.update(password.encode('utf-8'))
    # 返回十六进制表示的哈希值
    return sha256.hexdigest()


# 更改密码
def change_pwd(temp_flag):
    active = global_vars.active
    temp_id = False
    if temp_flag:  # 判断是不是管理员
        temp_id = simpledialog.askstring("输入","请输入需要修改的id")
        if temp_id is None:
            return
    temp_pwd = simpledialog.askstring("输入","请输入新密码")
    if temp_pwd is None:
        return
    try:
        active.change_pwd(temp_pwd, temp_id)
    except:
        if error_1():
            return
        else:
            change_pwd(temp_flag)

# 更新成绩
def update_score():
    # 这里懒了，就只写了一个id录入的方法
    student_id = simpledialog.askstring("输入","请输入需要修改的学生id")
    if student_id is None:
        return
    active = global_vars.active
    try:
        active.update_score_by_id(student_id)
        messagebox.showinfo("通知", "修改成功")
    except:
        if error_1():
            return
        else:
            update_score()
    return


# 录入成绩
def insert_score():
    active = global_vars.active
    root=tk.Tk()
    root.withdraw()
    while True:
        # 先做一个不考虑不存在的版本先
        insert_type=simpledialog.askstring("输入","请输入想要录入的方式:1.按班级 2.按学科 3.按id单独录入 输入0即可退出 ",parent=root)
        if insert_type is None:
            return
        if insert_type == '0':
            return
        temp = simpledialog.askstring("输入","请输入数据（选择学科的直接输入科目即可",parent=root)
        if temp is None:
            return
        try:
            if insert_type == '1':
                active.insert_score_by_class(temp)
            elif insert_type == '2':
                active.insert_score_by_subject(temp)
            elif insert_type == '3':
                active.insert_score_by_id(temp)
            else:
                if error_1():
                    return
                else:
                    continue
            messagebox.showinfo("通知", "录入成功")
            return
        except:
            if error_1():
                return
            else:
                continue


# 查询成绩
def select1():  # 检索成绩
    active = global_vars.active
    flag = global_vars.flag
    temp_flag = flag
    temp = None
    root=tk.Tk()
    root.withdraw()
    if flag != 1:
        temp_flag, temp = select2(root)
    if not active.select_score(temp_flag, temp):
        messagebox.showerror("输入数据有误,请重新来")
        select1()
    return


def select2(root):
    temp_flag = simpledialog.askstring("输入", "输入要以什么方式查询，不输入默认全部查询 1.学生学号 2.学生姓名 3.学生班级 4.语文 5.数学 6.英语", parent=root)
    if temp_flag is None:
        return
    flag = global_vars.flag
    if temp_flag == "":
        return flag, ""
    else:
        temp_flag = int(temp_flag) + 3

    if 4 <= temp_flag <= 9:
        if temp_flag>6:
            return temp_flag,None
        temp=simpledialog.askstring("输入", "输入要查询的数据", parent=root)
        if temp is None:
            return
        root.destroy()
        return temp_flag, temp
    else:
        print("输入有误")
        select2(root)


def ai():
    flag1=global_vars.flag
    active = global_vars.active
    score = active.return_score()
    api_key = global_vars.api_key
    def save(ans):
        with open('ai.txt', 'w', encoding='utf-8') as fp:
            fp.write(ans)
    if flag1==1:
        ans = f"你现在是一名老师，在下面会交给你一个列表，我现在要求你根据这个列表里面的完成一些简单的数理运算计算他们的平均绩点,假如某一科它的成绩不为正数，你无需理会这项数据，绩点计算方式为，x-50/10(如果x小于60则直接视为0），最后求他们的平均值,我在此命这个平均值为y（你无需告知我计算过程，只需要告知我每科的最终绩点）。然后你在根据你所计算的平均绩点合各科成绩给这名学生一点建议（不要超过100字)，倘若平均绩点y低于1.5则要发出警告“否则将无法毕业”，并且在末尾加一段名人警句来激励学生(无需在前面加上名人警句四个字！，名言警句要求直接换行输出即可）,列表当中的元素中的数据分别为学生id,姓名,班级,语文,数学,英语的成绩{score}.发送回来答案格式我要求你如下所示，[]表示我的注释，并不是我所要求的注释：语文（）数学（）英语（）[前面括号填写你所算的那科绩点这里换一行]平均绩点（）[换行，下面括号填写对学生的评价和建议]（）"
    elif flag1==2:
        ans = f""" 请计算以下数据集中每个班级的平均绩点，并给出针对教师的建议。数据如下：
                {score}
                计算平均绩点的规则如下：
                1. 绩点满分为5分。
                2. 计算公式为：绩点 = (成绩 - 60) / 10。
                3. 不足60分的成绩，绩点为0。
                4. 负数成绩表示该生未选修该门课程，忽略此成绩。
                请按照以下步骤操作：
                1. 计算每个学生的平均绩点。无需告知我
                2. 计算所有学生的平均绩点。无需告知我
                3. 给出针对教师的建议和成绩最好的那位学生和成绩最差的学生的栽培建议。
                (重要，必须遵守)如上的标题题目通通无需输出，只需要告诉结果即可"""
    url = "https://api.openai-sb.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "gpt-3.5-turbo",
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": ans,
            },
        ],
    }
    try:
        response = requests.post(url, headers=headers, json=body)
    except:
        print("请求失败,请联系管理员")
        return
    if response.status_code == 200:
        result = response.json()
        ans = result["choices"][0]['message']['content']
        root = tk.Tk()
        root.title("ai")
        root.geometry('600x300')
        text_area = scrolledtext.ScrolledText(root, width=60, height=20)
        text_area.grid(column=0, row=0)
        text_area.insert(tk.INSERT, "建议\n")
        text_area.insert(tk.INSERT,ans)


        save_button = tk.Button(root, text="保存", command=lambda: save(ans))
        save_button.grid(column=1, row=1)
        exit_button = tk.Button(root, text="退出", command=root.destroy)
        exit_button.grid(column=2, row=1)
        root.mainloop()
    else:
        print(f"请求失败，状态码：{response.status_code}")



def pingyin(s):
    s=str(s)
    s_pinyin = ''.join(lazy_pinyin(s))
    return s_pinyin
