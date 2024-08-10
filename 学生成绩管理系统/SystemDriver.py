import time
import pyodbc
from usually import *
from pypinyin import lazy_pinyin
import global_vars

class STUDENTS_MANAGEMENT_SYSTEM:
    # 初始化
    def __init__(self, user_name, pwd):
        # 创建连接字符串
        with open("config.txt", "r") as f:
            conn_str = f.read()
        try:
            # 连接到SQL Server
            self.pwd = pwd
            self.conn = pyodbc.connect(conn_str)
            # 判断是否登录成功
            if not self.__CheckPwd__(user_name):
                print("密码错误,请重新输入")
                return
            global_vars.login_flag = True
            self.id1 = self.__get_id__(user_name)
            # 分为教师端和学生端获取信息
            flag1 = int(self.id1) // 10000
            global_vars.flag = flag1
            # 管理员直接完成验证
            if flag1 == 9:
                self.name = "admit"
                return
            elif flag1 == 1:
                self.name = self.__get_stu_name__()
            else:
                self.name = self.__get_teacher_name__()
            return
        except:
            return

    # 获取唯一的id
    def __get_id__(self, user_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM account WHERE username = ? and password = ?", (user_name, self.pwd))
        row = cursor.fetchone()
        cursor.close()
        if row is not None:
            return row[0]
        else:
            exit(0)

    # 判断教师和学生两种不同可能出来
    def __get_stu_name__(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM StudentsId WHERE id = ?", (self.id1,))
        row = cursor.fetchone()
        cursor.close()
        if row is not None:
            return row[0]
        else:
            print("没有该用户信息")
            exit(0)

    # 获取教师名字
    def __get_teacher_name__(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM TeachersId WHERE id = ?", (self.id1,))
        row = cursor.fetchone()
        cursor.close()
        if row is not None:
            return row[0]
        else:
            print("没有该用户信息")
            exit(0)

    # 获取真实密码
    def __GetTruePwd__(self, user_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password FROM account WHERE username = ?", (user_name,))
        row = cursor.fetchone()
        cursor.close()
        return row[0]

    # 检查密码是否正确
    def __CheckPwd__(self, username):
        true_pwd = self.__GetTruePwd__(username)
        self.pwd = hash_password(self.pwd)
        return True if true_pwd == self.pwd else False

    # 获取成绩的模块
    def __get_score__(self, student_name):
        max_attempts = 3
        for attempt in range(max_attempts):
            print(f"请依次输入学生{student_name}的英语数学英语（若非科任老师直接可跳过）的成绩：")
            chinese = input("请输入语文的\n")
            if chinese == '':
                chinese = -1
            math = input("请输入数学的\n")
            if math == '':
                math = -1
            english = input("请输入英语的\n")
            if english == '':
                english = -1
            if chinese!=-1 or math!=-1 or english!=-1:
                return chinese, math, english
            else:
                print("你输入的数据有误，请重新输入")
        else:
            print("你已经尝试了3次，但是还是没有输入一个有效的成绩,系统已自动退出")
            return False

    # 获取当前用户的id和名字
    def get_info(self):
        return self.id1, self.name

    # 更改密码
    def change_pwd(self, new_pwd, temp_id):
        cursor = self.conn.cursor()
        # 用hash加密
        new_pwd = hash_password(new_pwd)
        if temp_id:
            cursor.execute("UPDATE account SET password = ? where id = ?", (new_pwd, temp_id))
        else:
            cursor.execute("UPDATE account SET password = ? where id = ?", (new_pwd, self.id1))
        self.conn.commit()
        cursor.close()

    # 查询成绩
    def select_score(self, flag1, temp=None):
        count = 0
        cursor = self.conn.cursor()
        try:
            # 这里到时候修一修
            if flag1 == 1:
                cursor.execute("SELECT * FROM students_score where id = ? and name = ?", (self.id1, self.name))
            elif flag1 == 2 or flag1 == 3:
                cursor.execute("SELECT * FROM students_score")
            elif flag1 == 4:
                cursor.execute("SELECT * FROM students_score where id = ?", (temp,))
            elif flag1 == 5:
                cursor.execute("SELECT * FROM students_score where name = ?", (temp,))
            elif flag1 == 6:
                cursor.execute("SELECT * FROM students_score where class = ?", (temp,))
            elif flag1 == 7:
                cursor.execute("SELECT * FROM students_score WHERE Chinese <> -1")
            elif flag1 == 8:
                cursor.execute("SELECT * FROM students_score WHERE Math <> -1")
            elif flag1 == 9:
                cursor.execute("SELECT * FROM students_score WHERE English <> -1")
            temp_list=[]
            print("学生学号 学生姓名 班级 语文 数学 英语 总分 平均绩点\t")
            for row in cursor:
                count += 1
                #算总分
                sum_score=str(sum(row[3:6]))
                avg_score=0
                #算绩点
                if row[3]<60:
                    avg_score+=0
                else:
                    avg_score+=(int(row[3])-50)/10
                if row[4]<60:
                    avg_score+=0
                else:
                    avg_score+=(int(row[4])-50)/10
                if row[5]<60:
                    avg_score+=0
                else:
                    avg_score+=(int(row[5])-50)/10
                avg_score=str(float('%.2f'%(avg_score/3)))
                row= str(row)
                temp_list.append(row+' '+sum_score+' '+avg_score)
                print(row+' '+sum_score+' '+avg_score)
            if input("是否保存？y/n\n")=='y':
                with open('score.txt','w',encoding='utf-8') as fp:
                    fp.write("学生学号 学生姓名 班级 语文 数学 英语 总分 平均绩点\t\n"+''.join(str(temp_list).replace('", "', '"\n"')))
            cursor.close()
            time.sleep(0.5)
            return 1
        except Exception as aaa:
            cursor.close()
            print(aaa)
            return 0

    # 实现按班级填入学生成绩
    def insert_score_by_class(self, class_name):
        cursor = self.conn.cursor()
        # 查询该班级的所有学生的id
        cursor.execute(f"SELECT id, name FROM StudentsId WHERE class = '{class_name}'")
        students_info = cursor.fetchall()
        students_id = [info[0] for info in students_info]
        students_name = [info[1] for info in students_info]

        for student_id, student_name in zip(students_id, students_name):
            # 对每个学生请求输入成绩
            chinese, math, english = self.__get_score__(student_name)
            # 插入到数据库中
            cursor.execute(
                "INSERT INTO students_score (id, name, class, Chinese, Math, English) VALUES (?, ?, ?, ?, ?, ?)",
                (student_id, student_name, class_name, chinese, math, english))

        self.conn.commit()
        cursor.close()

    # 实现按学科填入学生成绩
    def insert_score_by_subject(self, subject):
        cursor = self.conn.cursor()
        # 查询该学科的所有学生的id
        cursor.execute("SELECT id FROM lesson WHERE subject = ?", (subject,))
        students_id = [id[0] for id in cursor.fetchall()]

        # 同时查询名字和班级
        cursor.execute("SELECT name, class FROM StudentsId WHERE id in ({})".format(','.join('?' * len(students_id))),
                       students_id)
        students_info = cursor.fetchall()

        # 分别获取名字和班级
        students_name = [info[0] for info in students_info]
        students_class = [info[1] for info in students_info]

        for student_id, student_name, student_class in zip(students_id, students_name, students_class):
            # 对每个学生请求输入成绩
            chinese, math, english = self.__get_score__(student_name[0])
            # 插入到数据库中
            cursor.execute(
                "INSERT INTO students_score (id, name, class, Chinese, Math, English) VALUES (?, ?, ?, ?, ?, ?)",
                (student_id, student_name[0], student_class[0], chinese, math, english))

        self.conn.commit()
        cursor.close()

    # 实现按id填入学生成绩
    def insert_score_by_id(self, id1):
        # 名字
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, class FROM StudentsId WHERE id = ?", (id1,))
        result = cursor.fetchone()
        student_name = result[0]
        student_class = result[1]

        chinese, math, english = self.__get_score__(student_name)

        # 插入到数据库中
        cursor.execute(
            "INSERT INTO students_score (id, name, class, Chinese, Math, English) VALUES (?, ?, ?, ?, ?, ?)",
            (id1, student_name, student_class, chinese, math, english))

        self.conn.commit()
        cursor.close()

    # 实现修改成绩
    def update_score_by_id(self, id1):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM StudentsId WHERE id = ?", (id1,))
        students_name = cursor.fetchall()[0]
        cursor.close()

        Chinese, Math, English = self.__get_score__(students_name)
        cursor = self.conn.cursor()
        if Chinese != -1:
            cursor.execute("UPDATE students_score SET Chinese = ? WHERE id = ?", (Chinese, id1))
        if English != -1:
            cursor.execute("UPDATE students_score SET English = ? WHERE id = ?", (English, id1))
        if Math != -1:
            cursor.execute("UPDATE students_score SET Math = ? WHERE id = ?", (Math, id1))
        self.conn.commit()
        cursor.close()

    # 实现修改个人数据
    # 更改学生姓名
    def change_stu_name_info(self, id1):
        cursor = self.conn.cursor()
        temp = input("请输入更改后的数据\n")
        cursor.execute("UPDATE StudentsId SET name = ? WHERE id = ?", (temp, id1))
        self.conn.commit()
        cursor.close()

    # 更改教师姓名信息
    def change_tec_name_info(self, id1):
        cursor = self.conn.cursor()
        temp = input("请输入更改后的数据\n")
        cursor.execute("UPDATE TeachersId SET name=? WHERE id = ?", (temp, id1))
        cursor.close()

        cursor = self.conn.cursor()
        cursor.execute("UPDATE lesson SET teacher_name=? WHERE id = ?", (temp, id1))
        self.conn.commit()
        cursor.close()

    # 更改学生班级信息
    def change_class_info(self, id1):
        cursor = self.conn.cursor()
        temp = input("请输入更改后的数据\n")
        cursor.execute("UPDATE StudentsId SET class=? WHERE id = ?", (temp, id1))
        self.conn.commit()
        cursor.close()

    # 修改教师授课科目
    def change_deep_info(self, id1):
        cursor = self.conn.cursor()
        temp = input("请输入更改后的数据\n")
        cursor.execute("UPDATE TacherId SET deep=? WHERE id = ?", (temp, id1))
        cursor.close()

        cursor = self.conn.cursor()
        cursor.execute("UPDATE lesson SET subject=? WHERE id = ?", (temp, id1))
        self.conn.commit()
        cursor.close()

    # 获取成绩
    def return_score(self):
        flag1=global_vars.flag
        cursor = self.conn.cursor()
        if flag1==1:
            cursor.execute("SELECT * FROM students_score WHERE id = ?", (self.id1,))
        elif flag1==2:
            cursor.execute("SELECT students_score.id,name,class,Chinese,Math,English FROM students_score inner join lesson on students_score.id=lesson.id WHERE teacher_name = ?", (self.name,))
        temp = cursor.fetchall()
        cursor.close()
        return temp

    # 添加学生信息
    def add_stu_info(self, stu_id, stu_name, stu_class):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO StudentsId (id,name,class) VALUES (?, ?, ?)", (stu_id, stu_name, stu_class))

        cursor = self.conn.cursor()
        s_pinyin = pingyin(stu_name)
        print(f"已创建账号：{s_pinyin}，密码默认为123456")
        encoding_pwd = hash_password("123456")
        cursor.execute("INSERT INTO account (id,username,password) VALUES (?, ?, ?)", (stu_id, s_pinyin, encoding_pwd))

        self.conn.commit()
        cursor.close()

    # 添加教师信息
    def add_tec_info(self, tec_id, tec_name, tec_deep):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO TeachersId (id,name,deep) VALUES (?, ?, ?)", (tec_id, tec_name, tec_deep))

        cursor = self.conn.cursor()
        s = str(tec_name)
        s_pinyin = ''.join(lazy_pinyin(s))
        print(f"已创建账号：{s_pinyin}，密码默认为123456")
        encoding_pwd = hash_password("123456")
        cursor.execute("INSERT INTO account (id,username,password) VALUES (?, ?, ?)", (tec_id, s_pinyin, encoding_pwd))

        self.conn.commit()
        cursor.close()

    # 删除学生信息
    def del_stu_info(self):
        cursor = self.conn.cursor()
        stu_id = input("请输入学生id\n")
        cursor.execute("DELETE FROM StudentsId WHERE id = ?", (stu_id,))
        cursor.execute("DELETE FROM account WHERE id = ?", (stu_id,))
        cursor.execute("DELETE FROM students_score WHERE id = ?", (stu_id,))
        cursor.execute("DELETE FROM lesson WHERE id = ?", (stu_id,))
        self.conn.commit()

    # 删除教师信息
    def del_tec_info(self):
        cursor = self.conn.cursor()
        tec_id = input("请输入教师id\n")
        cursor.execute("DELETE FROM TeachersId WHERE id = ?", (tec_id,))
        cursor.execute("DELETE FROM account WHERE id = ?", (tec_id,))
        cursor.execute("DELETE FROM lesson WHERE id = ?", (tec_id,))
        self.conn.commit()
        cursor.close()

    # 添加课程
    def add_lesson(self):
        cursor = self.conn.cursor()
        student_id = input("请输入上课学生id\n")
        lesson_name = input("请输入课程名称\n")
        lesson_teacher = input("请输入授课老师\n")
        cursor.execute(
            "INSERT INTO lesson (id,subject,teacher_name) VALUES (?, ?, ?)", (student_id, lesson_name, lesson_teacher))
        self.conn.commit()
        cursor.close()

    # 删除课程
    def del_lesson(self):
        cursor = self.conn.cursor()
        student_id = input("请输入想要删除的学生id\n")
        lesson_name = input("请输入想要删除的课程名称\n")
        cursor.execute("DELETE FROM lesson WHERE id = ? and subject = ?", (student_id, lesson_name))
        self.conn.commit()
        cursor.close()

    # 修改课程信息
    def change_lesson(self):
        cursor = self.conn.cursor()
        student_id = input("请输入想要修改的学生id\n")
        change_type = input("请输入修改什么：1.修改课程名称 2.修改授课老师\n")
        if change_type == '1':
            before_lesson_name = input("请输入想要修改的课程名称\n")
            after_lesson_name = input("请输入想要成为的课程名称\n")
            cursor.execute(
                "UPDATE lesson SET subject = ? WHERE id = ? and subject = ?",
                (after_lesson_name, student_id, before_lesson_name))
        elif change_type == '2':
            before_lesson_teacher = input("请输入想要修改的授课老师\n")
            after_lesson_teacher = input("请输入想要成为的授课老师\n")
            cursor.execute(
                "UPDATE lesson SET teacher_name = ? WHERE id = ? and teacher_name = ?",
                (after_lesson_teacher, student_id, before_lesson_teacher))
        else:
            return False
        self.conn.commit()
        cursor.close()
        return True

    # 添加账号
    def add_account(self, add_id, username, pwd):
        cursor = self.conn.cursor()
        pwd = hash_password(pwd)
        try:
            cursor.execute("INSERT INTO account (id, username, password) VALUES (?, ?, ?)", (add_id, username, pwd))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as error:
            print(error)
            return False

