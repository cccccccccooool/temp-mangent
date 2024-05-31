from SystemDiver import *
from menu import *
import global_vars

teacher_account = [123]
student_account = [234]
admit_account = ["admit"]
flag = 0

# 反正也是个小小程序，所以对内存占用不会做任何优化，比如下面的代码会带来无限循环或无限递归的可能性
# 菜单
if __name__ == '__main__':
    while True:
        user_name = input("请输入账号")
        pwd = input("请输入密码")

        # 将账号标记为学生
        if user_name in student_account:
            flag = 1
        # 将账号标记为教师
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
        except:
            continue
        # 都不存在则为管理员
        menu()
