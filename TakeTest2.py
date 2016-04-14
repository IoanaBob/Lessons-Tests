import tkinter as tk
import json
from random import randint
from tkinter import font
LARGE_FONT= ("Verdana", 12)

with open('questions2.json', encoding="utf-8") as data_file:
    test_data = json.load(data_file)

class TakeTest2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from ViewLesson1 import ViewLesson1
        from ViewLesson2 import ViewLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from StartPage import StartPage
        from MainStudentPage import MainStudentPage
        from MyGrades import MyGrades

       # from TestPage1 import TestPage1
        from Test2Page0 import Test2Page0
        #=====================================
        # Menu
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu0 = tk.Button(self, text="Home", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainStudentPage))
        menu0.grid(row=0, column=0)
        menu0.configure(background = '#FF8800')
        menu1 = tk.Button(self, text="Probability Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson1))
        menu1.grid(row=0, column=1)
        menu1.configure(background = '#FF8800')
        menu2 = tk.Button(self, text="Sets Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson2))
        menu2.grid(row=0, column=2)
        menu2.configure(background = '#FF8800')
        menu3 = tk.Button(self, text="Probability Test", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(TakeTest1))
        menu3.grid(row=0, column=3)
        menu3.configure(background = '#FF8800')
        menu4 = tk.Button(self, text="Sets Test", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(TakeTest2))
        menu4.grid(row=0, column=4)
        menu5 = tk.Button(self, text="My Grades", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MyGrades))
        menu5.grid(row=0, column=5)
        menu5.configure(background = '#FF8800')
        menu6 = tk.Button(self, text="Back Home", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainStudentPage))
        menu6.grid(row=0, column=6)
        menu6.configure(background = '#FF8800')
        menu7 = tk.Button(self, text="Log Out", padx=4, pady=4, font=self.buttonFont,  relief=tk.RIDGE, command=lambda: controller.show_frame(StartPage))
        menu7.grid(row=0, column=7)
        menu7.configure(background = '#FF8800')
        #=====================================


        label = tk.Label(self, text="Are you ready to take the Sets test?", font=self.titleFont)
        label.grid(row=1, column=0, columnspan=20, sticky="W")
        label.configure(background = 'white')



        def combine_funcs():
            controller.refresh_frame(Test2Page0)
            controller.show_frame(Test2Page0)

        data = {"topic": 1, "score": 0}
        with open('current_score.json', 'w') as json_data:
            json.dump(data, json_data)

        menu6 = tk.Button(self, text="Take Sets Test", font=self.buttonFont, relief = tk.RIDGE, borderwidth = 4, padx=4, pady=4, command=lambda: combine_funcs())
        menu6.grid(row=2, column=0, columnspan=20, sticky="W")
