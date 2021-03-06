import tkinter as tk
import StudentLogin
from tkinter import font
import json

LARGE_FONT= ("Verdana", 12)

def get_user(self, controller):
    return StudentLogin.username

class MainStudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from ViewLesson1 import ViewLesson1
        from ViewLesson2 import ViewLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from StartPage import StartPage
        from MyGrades import MyGrades
        #=====================================
        # MENU STARTS HERE
        # TODO: make buttons stay one near each other (not depending on the other columns)
        #root.configure(background="alice blue")

        with open('current_user.json') as data_file:
            current_user = json.load(data_file)

        def combine_lesson1():
            controller.refresh_frame(ViewLesson1)
            controller.show_frame(ViewLesson1)

        def combine_lesson2():
            controller.refresh_frame(ViewLesson2)
            controller.show_frame(ViewLesson2)

        def combine_test1():
            controller.refresh_frame(TakeTest1)
            controller.show_frame(TakeTest1)

        def combine_test2():
            controller.refresh_frame(TakeTest2)
            controller.show_frame(TakeTest2)


        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        menu1 = tk.Button(self, text="Take Sets Lesson", borderwidth = 4, width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: combine_lesson2())
        menu1.grid(row=2, column=0)
        menu1.configure(background = '#FF8800')
        menu2 = tk.Button(self, text="Take Probability Lesson", borderwidth = 4, width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: combine_lesson1())
        menu2.grid(row=4, column=0)
        menu2.configure(background = '#FF8800')
        menu3 = tk.Button(self, text="Take Sets Test", borderwidth = 4, width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: combine_test2())
        menu3.grid(row=2, column=2)
        menu3.configure(background = '#FF8800')
        menu4 = tk.Button(self, text="Take Probability Test", borderwidth = 4, font=self.buttonFont, padx=4, pady=4, width=20, command=lambda: combine_test1())
        menu4.grid(row=4, column=2)
        menu4.configure(background = '#FF8800')
        menu5 = tk.Button(self, text="View My Grades", borderwidth = 4, width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(MyGrades))
        menu5.grid(row=6, column=0, columnspan=3)
        menu5.configure(background = '#FF8800')
        menu6 = tk.Button(self, text="Log Out", font=self.buttonFont, borderwidth = 4, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=10, column=0, columnspan=3)
        menu6.configure(background = '#FF8800')
        #=====================================

        text = "Welcome back " + str(current_user["username"]) + "!"

        label = tk.Label(self, text=text, font=self.headFont, padx=15, pady=5)

        label2 = tk.Label(self, text="Click on a button below.", font=self.titleFont, padx=5)
        label2.configure(background = 'white')

        blank_space = tk.Label(self, text="")
        blank_space.configure(background = 'white')
        blank_space1 = tk.Label(self, text="")
        blank_space1.configure(background = 'white')
        blank_space2 = tk.Label(self, text="")
        blank_space2.configure(background = 'white')
        label.grid(row=0, columnspan=2)
        label2.grid(row=1, columnspan=2)
        blank_space.grid(row=3 ,column = 1)
        blank_space1.grid(row=5, column = 1)
        blank_space2.grid(row=9, column = 1)
