import Student
import Teacher
import admit
import global_vars
active = global_vars.active
flag = global_vars.flag

def menu():
    while True:
        global  active,flag
        active = global_vars.active
        flag = global_vars.flag
        print("------------------")
        print("欢迎来到学生成绩管理系统")
        print('---------------------')
        now_id, now_name = active.get_info()
        print(f"欢迎你 {now_id}_{now_name}")
        print('---------------------')
        print("请输入对应编号来选择你想要进行的操作")
        if flag == 1:
            Student.main()
        elif flag == 2:
            Teacher.main()
        elif flag == 3:
            admit.main()
