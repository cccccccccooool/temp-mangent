from SystemDriver import *
from menu import *
import time
from  usually import *
#未来在这给他整个页面，开始输入一行登录密码，然后重绘页面即可     ---------已经不打算重绘了，好麻烦
#这里改进了认证flag，直接通过学生id来认证

if __name__ == '__main__':
    while True:
        username = input("请输入用户名\n")
        password = input("请输入密码\n")
        try:
            global_vars.active = STUDENTS_MANAGEMENT_SYSTEM(username, password)
            if not global_vars.login_flag:
                print("\n用户名或密码错误\n")
                os.system('cls')
                time.sleep(1)
            else:
                print("登录成功，正在跳转")
                time.sleep(0.5)
                os.system('cls')
                menu()
        except Exception as e:
            time.sleep(10)
            print(e)
            continue
