import os
import sys
import time

from usually import *
import global_vars
def change_info(temp_flag):
    # 懒得做合理性检测了，凡是主键id都不允许被修改
    active = global_vars.active
    while True:
        try:
            os.system('cls')
            print("当前仅支持修改\t1.名字和\t2.班别/授课科目")
            change_type = int(input("请选择一个\n"))
            if change_type not in [1, 2]:
                if error_1():
                    break
                else:
                    continue
            changed_id = input("请输入要被更改的人的id\n")
            if change_type == 1:
                if temp_flag:
                    active.change_tec_name_info(changed_id)
                else:
                    active.change_stu_name_info(changed_id)
            else:
                if temp_flag:
                    active.change_deep_info(changed_id)
                else:
                    active.change_class_info(changed_id)
        except Exception as error:
            print(error)
            if error_1():
                break
            else:
                continue
        break
    return


def add_info(teamFlag):
    active = global_vars.active
    while True:
        os.system('cls')
        try:
            if not teamFlag:
                stu_id=int(input("请输入学生id\n"))
                stu_name=input("请输入姓名\n")
                stu_class=input("请输入班级\n")
                active.add_stu_info(stu_id,stu_name,stu_class)
            else:
                tec_id = int(input("请输入教师id\n"))
                tec_name = input("请输入姓名\n")
                tec_deep = input("请输入授课科目\n")
                active.add_tec_info(tec_id, tec_name, tec_deep)
        except Exception as error:
            print(error)
            if error_1():
                break
            else:
                continue
        break
    return

def delete_info(teamFlag):
    active = global_vars.active
    while True:
        os.system('cls')
        try:
            if teamFlag:
                active.del_tec_info()
            else:
                active.del_stu_info()
        except Exception as error:
            print(error)
            if error_1():
                break
            else:
                continue
        break
    return

def add_lesson_info():
    active = global_vars.active
    while True:
        os.system('cls')
        try:
            active.add_lesson()
        except Exception as error:
            print(error)
            if error_1():
                break
            else:
                continue
        break
    return

def delete_lesson_info():
    active = global_vars.active
    while True:
        os.system('cls')
        try:
            active.del_lesson()
        except Exception as error:
            #print(error)
            if error_1():
                break
            else:
                continue
        break
    return

def change_lesson_info():
    active = global_vars.active
    while True:
        os.system('cls')
        try:
            if not active.change_lesson():
                if error_1():
                    break
                else:
                    continue
        except Exception as error:
            print(error)
            if error_1():
                break
            else:
                continue
        break
    return

def append_username():
    while True:
        os.system('cls')
        add_id = input("请输入添加的账号id\n")
        username = input("请输入添加的账号名\n")
        pwd = input("请输入添加的账号密码\n")
        active = global_vars.active
        if active.add_account(add_id,username,pwd):
            if input("是否继续添加账号？(y/n)\n") == 'y':
                continue
            break
        else:
            print("\n系统出错\n")
            if error_1():
                break
            else:
                continue

def main():
        print("1.添加登录账号")
        print('2.查询学生成绩')
        print("3.录入学生成绩")
        print("4.修改学生成绩")
        print("5.编辑学生信息")
        print("6.编辑教师信息")
        print("7.添加学生信息")
        print("8.添加教师信息")
        print("9.删除学生信息")
        print("10.删除教师信息")
        print("11.修改其他成员的账号密码")
        print("12.录入课程信息")
        print("13.修改课程信息")
        print("14.删除课程信息")
        print("0.退出成绩管理系统")
        try:
            get_request = int(input("请输入你想要进行的操作\n"))
        except:
            os.system('cls')
            print("请输入数字")
            time.sleep(0.5)
            os.system('cls')
            return
        if get_request == 0:
            print("已退出")
            time.sleep(0.5)
            sys.exit(0)

        elif get_request==1:
            append_username()
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 2:
            select1()
        elif get_request == 3:
            insert_score()
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 4:
            update_score()
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 5:
            change_info(0)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 6:
            change_info(1)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 7:
            add_info(0)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 8:
            add_info(1)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 9:
            delete_info(0)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 10:
            delete_info(1)
            print("操作已完成")
            print("删除成功")
            time.sleep(0.5)
        elif get_request == 11:
            print("操作已完成")
            print("修改成功")
            time.sleep(0.5)
        elif get_request == 12:
            add_lesson_info()
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 13:
            change_lesson_info()
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == 14:
            delete_lesson_info()
            print("操作已完成")
            time.sleep(0.5)
        else:
            print("\n输入数据有误,请重新来\n")
        os.system('cls')