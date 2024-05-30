from usually import *
from global_vars import *


def change_info(temp_flag):
    # 懒得做合理性检测了，凡是主键id都不允许被修改
    print("当前仅支持修改\t1.名字和\t2.班别/授课科目")
    change_type = input("请选择一个")
    if change_type not in [1, 2]:
        if error_1():
            return
        else:
            return change_info(temp_flag)
    changed_id = input("请输入要被更改的人的id")
    try:
        if change_type == 1:
            if temp_flag:
                active.change_tec_name_info(changed_id)
            else:
                active.change_stu_name_info(changed_id)
        else:
            if temp_flag:
                active.change_class_info(changed_id)
            else:
                active.change_deep_info(changed_id)
    except:
        if error_1():
            return
        else:
            change_info(temp_flag)


def add_info(flag):
    pass


def main():
    print('1.更改自己的密码')
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
    print("0.退出成绩管理系统")
    get_request = input("请输入你想要进行的活动")
    if get_request == 0:
        print("已退出")
    elif get_request == 1:
        change_pwd()
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
        pass
    elif get_request == 8:
        pass
    elif get_request == 9:
        pass
    elif get_request == 10:
        pass
    elif get_request == 11:
        pass
    else:
        print("你输入的有误，请重新输入")
    main()