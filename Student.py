from usually import *


def main():
    while True:
        print('1.更改自己的密码')
        print('2.查询自己成绩')
        print('3.ai分析')
        print("0.退出成绩管理系统")
        get_request = int(input("请输入你想要进行的操作\n"))
        if get_request == 0:
            print("已退出")
            exit(0)
        elif get_request == 1:
            change_pwd(0)
        elif get_request == 2:
            select1()
        elif get_request == 3:
            ai()
        else:
            print("输入有误，请重新输入")
        continue