import Student
import Teacher
import admit
from global_vars import *
def menu():
    while True:
        print("------------------")
        print("欢迎来到学生成绩管理系统")
        print('---------------------')
        now_id,now_name=active.get_info()
        print(f"欢迎你{now_id}_{now_name}")
        print('---------------------')
        print("请输入对应编号来选择你想要进行的操作")
        if flag==1:
            Student.main()
        elif flag==2:
            Teacher.main()
        elif flag==3:
            admit.main()
        """print('1.更改自己的密码')
        if flag == 1:
            print('2.查询自己成绩')
        elif flag == 2:
            print("2.查询学生成绩")
            # 这里用数据插入方法
            print("3.录入学生成绩")
            print("4.修改学生成绩")
        elif flag == 3:
            # 这里用数据修改方法
            print("2.查询学生成绩")
            # 这里用数据插入方法
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
        get_request = int(input())

        if get_request == 0:
            print("已退出")
        elif get_request == 1:
            change_name()
        elif get_request == 2:
            select1()
        # 限制学生端访问
        if flag == 1:
            print("你输入的有误，请重新输入")
            continue

        if get_request == 3:
            insert_score()
        elif get_request==4:
            update_score()

        # 限制教师端访问
        if flag == 2:
            print("你输入的有误，请重新输入")
            continue

        if get_request == 5:
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
        continue
"""
