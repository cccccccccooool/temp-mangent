import hashlib
from global_vars import *
#报错统一模板
def error_1():
    get = input("输入有误，请重新输入,输入任意继续,输入0则退出当前模式")
    if get == "0":
        return True
    return False
#hash加密
def hash_password(password):
    # 创建一个新的哈希对象
    sha256 = hashlib.sha256()
    # 使用给定的密码更新哈希对象
    sha256.update(password.encode('utf-8'))
    # 返回十六进制表示的哈希值
    return sha256.hexdigest()

#更改密码
def change_pwd():
    active.change_pwd(str(input("请输入你想更改的密码")))

#更新成绩
def update_score():
    #这里懒了，就只写了一个id录入的方法
    student_id=input("请输入需要修改的学生id")
    try:
        active.update_score_by_id(student_id)
    except:
        if error_1():
            return
        else:
            update_score()
    return
#录入成绩
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
#查询成绩
def select1():
    temp_flag = flag
    temp = None
    if flag != 1:
        print("输入要以什么方式查询，不输入默认全部查询\t1.学生学号\t2.学生姓名\t3.学生班级\t4.语文\t5.数学\t6.英语")
        temp_flag,temp=select2()
    if not active.select_score(temp_flag, temp):
        print("输入数据有误,请重新来")
        select1()


def select2():
    temp_flag = input()
    if temp_flag == "":
        return flag,""
    else:
        temp_flag = int(temp_flag) + 3

    if 4 <= temp_flag <= 9:
        temp = str(input("请输入要查询内容"))
        return temp_flag,temp
    else:
        print("输入有误")
        select2()
