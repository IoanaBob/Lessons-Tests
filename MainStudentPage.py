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

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        menu1 = tk.Button(self, text="Take Sets Lesson", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(ViewLesson2))
        menu1.grid(row=2, column=0)
        menu2 = tk.Button(self, text="Take Probability Lesson", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(ViewLesson1))
        menu2.grid(row=3, column=0)
        menu3 = tk.Button(self, text="Take Sets Test", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(TakeTest1))
        menu3.grid(row=2, column=1)
        menu4 = tk.Button(self, text="Take Probability Test", font=self.buttonFont, padx=4, pady=4, width=20, command=lambda: controller.show_frame(TakeTest2))
        menu4.grid(row=3, column=1)
        menu5 = tk.Button(self, text="View My Grades", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(ViewLesson2))
        menu5.grid(row=6, column=0, columnspan=2)
        menu6 = tk.Button(self, text="Log Out", font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=8, column=0, columnspan=2)
        menu7 = tk.Button(self, text="Get User Name", font=self.buttonFont, padx=4, pady=4, command=lambda: print(get_user(self, controller)))
        menu7.grid(row=9, column=0, columnspan=2)
        #=====================================

        username = ""

        with open('users.json') as data_file:
            user_data = json.load(data_file)
        for user in user_data["Students"]:
            if get_user(self, controller) == user:
                username = user



        welcome_message = "Welcome back " + str(username) + "!"
        label = tk.Label(self, text=welcome_message, font=self.headFont, padx=15, pady=5)
        label2 = tk.Label(self, text="Click on a button below.", font=self.titleFont, padx=5)
        blank_space = tk.Label(self, text="", font=LARGE_FONT)
        label.grid(row=0, columnspan=2)
        label2.grid(row=1, columnspan=2)
        blank_space.grid(row=7)
