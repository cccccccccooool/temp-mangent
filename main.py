import pyodbc

teacher_account = []
student_account = []
flag = 3


class students_management_system():
    def __init__(self, user_name, pwd):
        # 创建连接字符串
        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=SIHASIHA;'  # 服务器名称
            r'DATABASE=Teach;'  # 数据库名称
            rf'UID={user_name};'  # 用户名
            fr'PWD={pwd};'  # 密码
        )
        try:
            # 连接到SQL Server
            self.conn=pyodbc.connect(conn_str)
            print("连接成功")
        except:
            print("连接失败")
            exit(0)
        self.id=self.__get_user_id__(user_name,pwd)
    #获取唯一的id
    def __get_user_id__(self, user_name,pwd):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id FROM account WHERE username = '{user_name}' and password='{pwd}'")
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            exit(0)
    #更改昵称
    def change_name(self, new_name):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE all_id SET name = '{new_name}' where id='{self.id}'")
        self.conn.commit()
    #查询成绩
    def select_score(self,flag,temp=None):
        count=0
        cursor = self.conn.cursor()
        try:
            if flag==1:
                cursor.execute(f"SELECT * FROM student_achievement where id = '{self.id}'")
            elif flag==2 or flag==3:
                cursor.execute(f"SELECT * FROM student_achievement")
            elif flag==4:
                cursor.execute(f"SELECT * FROM student_achievement where id = '{self.id}' where id ={temp}")
            elif flag==5:
                cursor.execute(f"SELECT * FROM student_achievement where id = '{self.id}' where name ={temp}")
            elif flag==6:
                cursor.execute(f"SELECT * FROM student_achievement where id = '{self.id}' where class ={temp}")
            elif flag==7:
                cursor.execute(f"SELECT * FROM student_achievement where id = '{self.id}' where teacher_name ={temp}")
            for row in cursor:
                count+=1
                print(row,'\t')
                if count%4==0:
                    print('\n')
            return 1
        except:
            return 0

#菜单
def menu():
    print("------------------")
    print("欢迎来到学生成绩管理系统")
    print('---------------------')
    print("请输入对应编号来选择你想要进行的操作")
    print('1.编辑自己的昵称')
    if flag == 1:
        print('2.查询自己成绩')
    elif flag >= 2:
        print("2.查询学生成绩")
        #这里用数据插入方法
        print("3.录入学生成绩")
    elif flag >= 3:
        #这里用数据修改方法
        print("4.编辑学生信息")
        print("5.编辑教师信息")
        print("6.添加学生信息")
        print("7.添加教师信息")
        print("8.删除学生信息")
        print("9.删除教师信息")
        print("10.修改其他成员的昵称")
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
        menu()
    if get_request == 3:
        pass
    # 限制教师端访问
    if flag == 2:
        print("你输入的有误，请重新输入")
        menu()

    if get_request == 5:
        pass
    elif get_request == 6:
        pass
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
        menu()
def change_name():
    active.change_name(str(input("请输入你想更改的名字")))

def select1():
    temp_flag = flag
    temp = None
    if flag != 1:
        print("输入要以什么方式查询，不输入默认全部查询\t1.学生学号\t2.学生姓名\t3.学生班级\t4.任课老师")
        select2()
    if not active.select_score(temp_flag, temp):
        print("输入数据有误,请重新来")
        select1()

def select2():
    temp_flag = input()
    if temp_flag == "":
        return
    else:
        temp_flag = int(temp_flag) + 3
    if 4 <= temp_flag <= 7:
        temp = str(input("请输入要查询内容"))
        return temp
    else:
        print("输入有误")
        select2()

if __name__ == '__main__':
    user_name = input("请输入账号")
    pwd = input("请输入密码")
    name=input("请输入")
    active = students_management_system(user_name, pwd)

    # 将账号标记为学生
    if user_name in student_account:
        flag = 1
    # 将账号标记为教师
    elif user_name in teacher_account:
        flag = 2
    # 都不存在则为管理员
    menu()