import tkinter as tk
import json
from TakeTest2 import TakeTest2
from tkinter import font
LARGE_FONT= ("Verdana", 12)

with open('lessons.json', encoding="utf-8") as data_file:
    lesson_data = json.load(data_file)

class ViewLesson2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from ViewLesson1 import ViewLesson1
        from ViewLesson2 import ViewLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from StartPage import StartPage
        from MainStudentPage import MainStudentPage
        from MyGrades import MyGrades
        #=====================================
        # MENU STARTS HERE
        # TODO: make buttons stay one near each other (not depending on the other columns)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        menu0 = tk.Button(self, text="Home", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainStudentPage))
        menu0.grid(row=0, column=0)
        menu0.configure(background = '#FF8800')
        menu1 = tk.Button(self, text="Probability Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson1))
        menu1.grid(row=0, column=1)
        menu1.configure(background = '#FF8800')
        menu2 = tk.Button(self, text="Sets Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson2))
        menu2.grid(row=0, column=2)
        menu3 = tk.Button(self, text="Probability Test", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(TakeTest1))
        menu3.grid(row=0, column=3)
        menu3.configure(background = '#FF8800')
        menu4 = tk.Button(self, text="Sets Test", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(TakeTest2))
        menu4.grid(row=0, column=4)
        menu4.configure(background = '#FF8800')
        menu5 = tk.Button(self, text="My Grades", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MyGrades))
        menu5.grid(row=0, column=5)
        menu5.configure(background = '#FF8800')
        menu6 = tk.Button(self, text="Back Home", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainStudentPage))
        menu6.grid(row=0, column=6)
        menu6.configure(background = '#FF8800')
        menu7 = tk.Button(self, text="Log Out", padx=4, pady=4, font=self.buttonFont,  relief=tk.RIDGE, command=lambda: controller.show_frame(StartPage))
        menu7.grid(row=0, column=6)
        menu7.configure(background = '#FF8800')
        #=====================================

        label = tk.Label(self, text=lesson_data['Lessons'][1]['Lesson Title'], font=self.headFont)
        label.grid(row=1, columnspan=2)
        label.configure(background = 'white')

        text = tk.Text(self, font=self.textFont)
        text.insert(tk.INSERT, lesson_data['Lessons'][1]['Lesson Content'])

        text.config(state=tk.DISABLED)
        text.grid(row=2, columnspan=8)

        # Go to take test
        button1 = tk.Button(self, text="Continue and take test on sets", font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(TakeTest2))
        button1.grid(row=3, columnspan=8)
        button1.configure(background = '#FF8800')
