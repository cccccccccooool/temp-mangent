from usually import *
import global_vars
def change_info(temp_flag):
    # 懒得做合理性检测了，凡是主键id都不允许被修改
    active = global_vars.active
    print("当前仅支持修改\t1.名字和\t2.班别/授课科目")
    change_type = int(input("请选择一个\n"))
    if change_type not in [1, 2]:
        if error_1():
            return
        else:
            return change_info(temp_flag)
    changed_id = input("请输入要被更改的人的id\n")
    try:
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
            return
        else:
            change_info(temp_flag)


def add_info(teamFlag):
    active = global_vars.active
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
            return
        else:
            add_info(teamFlag)

def delete_info(teamFlag):
    active = global_vars.active
    try:
        if teamFlag:
            active.del_tec_info()
        else:
            active.del_stu_info()
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            delete_info(teamFlag)

def add_lesson_info():
    active = global_vars.active
    try:
        active.add_lesson()
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            add_lesson_info()

def delete_lesson_info():
    active = global_vars.active
    try:
        active.del_lesson()
    except Exception as error:
        #print(error)
        if error_1():
            return
        else:
            delete_lesson_info()

def change_lesson_info():
    active = global_vars.active
    try:
        active.change_lesson()
    except Exception as error:
        print(error)
        if error_1():
            return
        else:
            change_lesson_info()

def append_username(add_id,username,pwd,temp_flag):
    active = global_vars.active
    if active.add_account(add_id,username,pwd):
        return
    else:
        print("系统出错")
        if error_1():
            return
        else:
            append_username(add_id,username,pwd,temp_flag)

def main():
    while True:
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
        get_request = int(input("请输入你想要进行的操作"))
        if get_request == 0:
            print("已退出")
            exit(0)
        elif get_request==1:
            if input("要添加1.学生还是2.教师信息：\n")=='1':
                append_username(int(input("请输入学生id\n")),input("请输入账号\n"),input("请输入明文密码\n"),1)
            else:
                append_username(int(input("请输入教师id\n")),input("请输入账号\n"),input("请输入明文密码\n"),0)
        elif get_request == 2:
            select1()
        elif get_request == 3:
            insert_score()
        elif get_request == 4:
            update_score()
        elif get_request == 5:
            change_info(0)
        elif get_request == 6:
            change_info(1)
        elif get_request == 7:
            add_info(0)
        elif get_request == 8:
            add_info(1)
        elif get_request == 9:
            delete_info(0)
        elif get_request == 10:
            delete_info(1)
        elif get_request == 11:
            change_pwd(1)
        elif get_request == 12:
            add_lesson_info()
        elif get_request == 13:
            change_lesson_info()
        elif get_request == 14:
            delete_lesson_info()
        else:
            print("你输入的有误，请重新输入")
        continue