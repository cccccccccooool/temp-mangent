from usually import *
def main():
    print('1.更改自己的密码')
    print('2.查询自己成绩')
    print("0.退出成绩管理系统")
    get_request=input("请输入你想要进行的活动")
    if get_request == 0:
        print("已退出")
    elif get_request == 1:
        change_pwd()
    elif get_request == 2:
        select1()
    else:
        print("输入有误，请重新输入")
        return main()