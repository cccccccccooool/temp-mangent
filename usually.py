import hashlib
import requests
import global_vars
active = global_vars.active
flag = global_vars.flag
api_key=global_vars.api_key

# 报错统一模板
def error_1():
    get = input("输入有误，请重新输入,输入任意继续,输入0则退出当前模式")
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
    temp_id = False
    if temp_flag:  # 判断是不是管理员
        temp_id = input("请输入需要修改的id")
    temp_pwd = input("请输入新密码")
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
    student_id = input("请输入需要修改的学生id")
    try:
        active.update_score_by_id(student_id)
    except:
        if error_1():
            return
        else:
            update_score()
    return


# 录入成绩
def insert_score():
    while True:
        # 先做一个不考虑不存在的版本先
        insert_type = input("请输入想要录入的方式：\t1.按班级\t2.按学科\t3.按id单独录入")
        temp = input("请输入数据（选择学科的直接输入科目即可")
        try:
            if insert_type == 1:
                active.insert_score_by_class(temp)
            elif insert_type == 2:
                active.insert_score_by_subject(temp)
            elif insert_type == 3:
                active.insert_score_by_id(temp)
            else:
                if error_1():
                    return
                else:
                    continue
        except:
            if error_1():
                return
            else:
                continue


# 查询成绩
def select1():  # 检索成绩
    temp_flag = flag
    temp = None
    if flag != 1:
        print("输入要以什么方式查询，不输入默认全部查询\t1.学生学号\t2.学生姓名\t3.学生班级\t4.语文\t5.数学\t6.英语")
        temp_flag, temp = select2()
    if not active.select_score(temp_flag, temp):
        print("输入数据有误,请重新来")
        select1()


def select2():
    temp_flag = input()
    if temp_flag == "":
        return flag, ""
    else:
        temp_flag = int(temp_flag) + 3

    if 4 <= temp_flag <= 9:
        temp = str(input("请输入要查询内容"))
        return temp_flag, temp
    else:
        print("输入有误")
        select2()


def ai():
    score = active.get_score()
    ans = f"你现在是一名老师，在下面会交给你一个列表，我现在要求你根据这个列表里面的完成一些简单的数理运算计算他们的平均绩点，绩点计算方式为，x-60/10(如果结果为负数就视为该值为0），最后求他们的平均值（你无需告知我计算过程，只需要告知我每科的最终绩点）。然后你在根据你所计算的平均绩点合各科成绩给这名学生一点建议（不要超过100字),也可以选择在末尾加一段名人警句来激励学生(无需在前面加上名人警句四个字，直接输出即可）,现在默认输入三个数字，分别为语文数学英语的成绩{score}"
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
        choices = result["choices"][0]['message']['content']
        print(f"答案：{choices}")
    else:
        print(f"请求失败，状态码：{response.status_code}")
