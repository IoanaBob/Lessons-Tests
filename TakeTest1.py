import tkinter as tk
import json
from random import randint
from tkinter import font
LARGE_FONT= ("Verdana", 12)

with open('questions.json', encoding="utf-8") as data_file:
    test_data = json.load(data_file)

class TakeTest1(tk.Frame):

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
        from TestPage0 import TestPage0
        #=====================================
        # Menu
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu0 = tk.Button(self, text="Home", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainStudentPage))
        menu0.grid(row=0, column=0)
        menu0.configure(background = '#FF8800')
        menu1 = tk.Button(self, text="Probability Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson1))
        menu1.grid(row=0, column=1)
        menu2 = tk.Button(self, text="Sets Lesson", padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(ViewLesson2))
        menu2.grid(row=0, column=2)
        menu2.configure(background = '#FF8800')
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
        menu7.grid(row=0, column=7)
        menu7.configure(background = '#FF8800')
        #=====================================


        label = tk.Label(self, text="Are you ready to take the test?", font=self.titleFont)
        label.grid(row=1, column=0, columnspan=20, sticky="W")


       # menu6 = tk.Button(self, text="Take Test 1", command=lambda: controller.show_frame(TestPage1))
       # menu6.grid(row=2, column=5)
        #=====================================
        # label = tk.Label(self, text=test_data['Questions'][index]['Question Header'], font=LARGE_FONT)
        # label.grid(row=0)
        #
        # param = randint(0,len(test_data['Questions'][index]['Question Content'])-1)
        #
        # # label = tk.Label(self, text=test_data['Questions'][index]['Question Content'][param]['Question'], font=LARGE_FONT)
        # label.grid(row=1)
        #
        # answers = test_data['Questions'][index]['Question Content'][param]['Answers']
        # j = 0
        # for answer in answers:
        #     label = tk.Label(self, text=answer, font=LARGE_FONT)
        #     label.grid(row=2, column=j)
        #     j += 1
        #
        #
        # if index < (len(test_data['Questions']) - 1):
        #     next = tk.Button(self, text="Lesson 1", command=lambda: controller.show_frame(TestPages(index+1, parent, controller)))
        #     next.grid(row=3, column=0)

        #=====================================

        #for all Questions
        # display topic
        # randomly select question
        # display question header concatenated with question content
        # display answers as radio buttons



       # for i in range(0, len(test_data['Questions'])):
           # label = tk.Label(self, text=test_data['Questions'][i]['Question Topic'])
           # label.grid(row=i+4)
           # concat_text = test_data['Questions'][i]['Question Header'] + test_data['Questions'][i]['Question Content'][0]['Question']
           # label = tk.Label(self, text=concat_text)
           # label.grid(row=i+8)

            # fix this



        # # label = tk.Label(self, text = test_data['Questions'][])
        # vsb = tk.Scrollbar(self, orient="vertical")
        # text = tk.Text(self, width=40, height=20, yscrollcommand=self)
        #
        # # vsb.config(command=self.text.yview)
        # # vsb.pack(side="right", fill="y")
        # # text.pack(side="left", fill="both", expand=True)
        #
        # for i in range(10):
        #     cb = tk.Checkbutton(self, text="checkbutton #%s" % i)
        #     text.window_create("end", window=cb)
        #     text.insert("end", "\n") # to force one checkbox per line
        #
        #
        def combine_funcs():
            controller.refresh_frame(TestPage0)
            controller.show_frame(TestPage0)

        data = {"topic": 1, "score": 0}
        with open('current_score.json', 'w') as json_data:
            json.dump(data, json_data)

        menu6 = tk.Button(self, text="Take Probability Test", font=self.buttonFont, padx=4, pady=4, command=lambda: combine_funcs())
        menu6.grid(row=2, column=0, columnspan=20, sticky="W")
