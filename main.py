from SystemDriver import *
from menu import *
import global_vars

teacher_account = [123]
student_account = [234]
admit_account = ["admit"]
#管理员默认密码123456
flag = 0

if __name__ == '__main__':
    while True:
        user_name = input("请输入账号")
        pwd =input("请输入密码")

        if user_name in student_account:
            flag = 1
        elif user_name in teacher_account:
            flag = 2
        elif user_name in admit_account:
            flag = 3
        else:
            print("账号未被记录,请联系管理员增添")
            continue

        try:
            global_vars.active = STUDENTS_MANAGEMENT_SYSTEM(user_name, pwd, flag)
            global_vars.flag = flag
        except Exception as e:
            print(f"Error: {e}")
            continue

        menu()
