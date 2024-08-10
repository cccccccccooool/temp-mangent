import time
import Student
import Teacher
import admit
import global_vars
import tkinter as tk
import sys

def menu():
        flag = global_vars.flag
        if flag == 1:
            Student.main()
        elif flag == 2:
            Teacher.main()
        elif flag ==9:
            admit.main()

