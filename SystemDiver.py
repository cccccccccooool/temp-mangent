import pyodbc
from usually import *

class students_management_system():
    def __init__(self, user_name, pwd,flag):
        # 创建连接字符串
        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=SIHASIHA;'  # 服务器名称
            r'DATABASE=Teach;'  # 数据库名称
            rf'UID=sa;'  # 用户名
            fr'PWD=123456;'  # 密码
        )
        try:
            # 连接到SQL Server
            #管理员直接完成验证
            self.conn = pyodbc.connect(conn_str)
            if flag==3:
                self.id1="114514"
                self.name="admit"
                return

            if not self.__CheckPwd__(user_name,pwd):
                print("密码错误,请重新输入")
                return
            self.id1 = self.__get_id__(user_name, pwd)
            #分为教师端和学生端获取信息
            if flag==1:
                self.name=self.__get_stu_name__()
            else:
                self.name=self.__get_teacher_name__()
            return
        except:
            print("账号错误,请重新输入")
            return

    # 获取唯一的id
    def __get_id__(self, user_name, pwd):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id FROM account WHERE username = '{user_name}' and password='{pwd}'")
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            exit(0)

    #判断教师和学生两种不同可能出来
    def __get_stu_name__(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM StudentsId WHERE id = '{self.id1}'")
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            exit(0)

    def __get_teacher_name__(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM TeachersId WHERE id = '{self.id1}'")
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            exit(0)

    def __GetTruePwd__(self,user_name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT password FROM account WHERE username = '{user_name}'")
        row = cursor.fetchone()
        return row[0]

    def __CheckPwd__(self,username,pwd):
        true_pwd=self.__GetTruePwd__(username)
        pwd=hash_password(pwd)
        return True if true_pwd==pwd else False

    # 获取成绩的模块
    def __get_score__(self, student_name):
        max_attempts = 3
        for attempt in range(max_attempts):
            print(f"请依次输入学生{student_name}的英语数学英语（若非科任老师直接可跳过）的成绩：")
            chinese = input("请输入语文的")
            math = input("请输入数学的")
            english = input("请输入英语的")
            if chinese.isdigit() and math.isdigit() and english.isdigit() and 0 <= int(chinese) <= 100 and 0 <= int(math) <= 100 and 0 <= int(english) <= 100:
                return chinese, math, english
            else:
                print("你输入的数据有误，请重新输入")
        else:
            print("你已经尝试了3次，但是还是没有输入一个有效的成绩,系统已自动退出")
            return False


    #获取当前用户的id和名字
    def get_info(self):
        return self.id1,self.name

    # 更改密码
    def change_pwd(self, new_pwd):
        cursor = self.conn.cursor()
        #用hash加密
        new_pwd=hash_password(new_pwd)
        cursor.execute(f"UPDATE account SET password = '{new_pwd}' where id='{self.id1}'")
        self.conn.commit()

    # 查询成绩
    def select_score(self, flag, temp=None):
        count = 0
        cursor = self.conn.cursor()
        try:
            # 这里到时候修一修
            if flag == 1:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' and name = '{self.name}'")
            elif flag == 2 or flag == 3:
                cursor.execute(f"SELECT * FROM students_score")
            elif flag == 4:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where id ={temp}")
            elif flag == 5:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where name ={temp}")
            elif flag == 6:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where class ={temp}")
            elif flag == 7:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where Chinese ={temp}")
            elif flag == 8:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where Math ={temp}")
            elif flag == 9:
                cursor.execute(f"SELECT * FROM students_score where id = '{self.id1}' where English ={temp}")
            for row in cursor:
                count += 1
                print(row,end='\t')
                if count % 6 == 0:
                    print('\n')
            return 1
        except:
            return 0

    # 实现按班级填入学生成绩
    def insert_score_by_class(self, class_name):
        cursor = self.conn.cursor()
        # 查询该班级的所有学生的id
        cursor.execute(f"SELECT id FROM StudentsId WHERE class = '{class_name}'")
        students_id = cursor.fetchall()
        cursor.close()
        # 查询名字
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM StudentsId WHERE class = '{class_name}'")
        students_name = cursor.fetchall()
        # 获取当前所填写信息老师所授科目
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT deep FROM TacherId WHERE id = '{self.id1}'")
        teacher_name = cursor.fetchall()[0]

        for student_id, student_name in zip(students_id, students_name):
            # 对每个学生请求输入成绩
            chinese,math,english = self.__get_score__(student_name)
            # 插入到数据库中
            cursor.execute(
                f"INSERT INTO students_score (id, name,class,Chinese,Math,English) VALUES ('{student_id}', '{student_name}', '{class_name}',{chinese},{math},{english})")

        self.conn.commit()

    def insert_score_by_subject(self, subject):
        cursor = self.conn.cursor()
        # 查询该学科的所有学生的id
        cursor.execute(f"SELECT id FROM lesson WHERE subject = '{subject}'")
        students_id = cursor.fetchall()
        cursor.close()
        # 查询名字
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM StudentsId WHERE id in '{students_id}'")
        students_name = cursor.fetchall()
        # 查询班级
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT class FROM StudentsId WHERE id in '{students_id}'")
        students_class = cursor.fetchall()

        for student_id, student_name, student_class in zip(students_id, students_name, students_class):
            # 对每个学生请求输入成绩
            chinese,math,english = self.__get_score__(student_name)
            # 插入到数据库中
            cursor.execute(
                f"INSERT INTO students_score (id, name,class,Chinese,Math,English) VALUES ('{student_id}', '{student_name}', '{student_class}',{chinese},{math},{english})")

        self.conn.commit()

    def insert_score_by_id(self,id1):
        #名字
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM StudentsId WHERE id in '{id1}'")
        student_name = cursor.fetchall()[0]
        #班级
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT class FROM StudentsId WHERE id in '{id1}'")
        student_class = cursor.fetchall()[0]

        chinese, math, english = self.__get_score__(student_name)
        # 插入到数据库中
        cursor.execute(
            f"INSERT INTO students_score (id, name,class,Chinese,Math,English) VALUES ('{id1}', '{student_name}', '{student_class}',{chinese},{math},{english})")

        self.conn.commit()

    # 实现修改成绩
    def update_score_by_id(self, id1):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT name FROM all_id WHERE id in '{id1}'")
        students_name = cursor.fetchall()[0]

        score=self.__get_score__(students_name)
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE students_score SET score = {score} WHERE id = {id1}")
        self.conn.commit()
    #实现修改个人数据
    def change_stu_name_info(self,id1):
        cursor=self.conn.cursor()
        temp=input("请输入更改后的数据")
        cursor.execute(f"UPDATE StudentsId SET name={temp} WHERE id = {id1}")
        self.conn.commit()
        # 当发现修改的是教师信息的时候，也会将lesson这个表上的教师信息进行修改

    def change_tec_name_info(self, id1):
        cursor=self.conn.cursor()
        temp=input("请输入更改后的数据")
        cursor.execute(f"UPDATE TacherId SET name={temp} WHERE id = {id1}")
        self.conn.commit()

        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE lesson SET teacher_name={temp} WHERE id = {id1}")
        self.conn.commit()
    #更改学生班级信息
    def change_class_info(self,id1):
        cursor = self.conn.cursor()
        temp=input("请输入更改后的数据")
        cursor.execute(f"UPDATE StudentsId SET class={temp} WHERE id = {id1}")
        self.conn.commit()
    #修改教师授课科目
    def change_deep_info(self,id1):
        cursor = self.conn.cursor()
        temp=input("请输入更改后的数据")
        cursor.execute(f"UPDATE TacherId SET deep={temp} WHERE id = {id1}")
        self.conn.commit()

        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE lesson SET subject={temp} WHERE id = {id1}")
        self.conn.commit()