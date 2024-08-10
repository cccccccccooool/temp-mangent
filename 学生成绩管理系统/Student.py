import os
import sys
import time
from usually import *


def main():
        print('1.更改自己的密码')
        print('2.查询自己成绩')
        print('3.ai分析')
        print("0.退出成绩管理系统")
        get_request = input("请输入你想要进行的操作\n")
        if get_request == '0':
            print("已退出")
            sys.exit(0)
        elif get_request == '1':
            change_pwd(0)
            print("操作已完成")
            time.sleep(0.5)
        elif get_request == '2':
            select1()
        elif get_request == '3':
            ans = ai()
            if input("是否将结果保存？y/n") == 'y':
                with open("ai_stu.txt", 'w', encoding='utf-8') as fp:
                    fp.write(ans)
                print("保存成功")
            time.sleep(0.5)
        else:
            print("\n输入有误,请重新来\n")
        os.system('cls')
