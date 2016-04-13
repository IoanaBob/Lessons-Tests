import tkinter as tk
import json
from random import randint
LARGE_FONT= ("Verdana", 12)

with open('questions.json') as data_file:
    test_data = json.load(data_file)

class TakeTest1(tk.Frame):

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
<<<<<<< HEAD
        from TestPage1 import TestPage1
=======
        from TestPages import TestPages

>>>>>>> 16ce6beb21e96bacee5e1fe96a41a61fcb6a0672
        #=====================================
        # Menu
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu1 = tk.Button(self, text="Lesson 1", command=lambda: controller.show_frame(ViewLesson1))
        menu1.grid(row=0, column=0)
        menu2 = tk.Button(self, text="Lesson 2", command=lambda: controller.show_frame(ViewLesson2))
        menu2.grid(row=0, column=1)
        menu3 = tk.Button(self, text="Test 1", command=lambda: controller.show_frame(TakeTest1))
        menu3.grid(row=0, column=2)
        menu4 = tk.Button(self, text="Test 2", command=lambda: controller.show_frame(TakeTest2))
        menu4.grid(row=0, column=3)
        menu5 = tk.Button(self, text="My Grades", command=lambda: controller.show_frame(MyGrades))
        menu5.grid(row=0, column=4)
        menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=0, column=5)
        #=====================================


        label = tk.Label(self, text="Display Quesions", font=LARGE_FONT)
        label.grid(row=1)

<<<<<<< HEAD
        menu6 = tk.Button(self, text="Take Test 1", command=lambda: controller.show_frame(TestPage1))
        menu6.grid(row=2, column=5)
=======
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



        for i in range(0, len(test_data['Questions'])):
            label = tk.Label(self, text=test_data['Questions'][i]['Question Topic'])
            label.grid(row=i+4)
            concat_text = test_data['Questions'][i]['Question Header'] + test_data['Questions'][i]['Question Content'][0]['Question']
            label = tk.Label(self, text=concat_text)
            label.grid(row=i+8)

            # fix this 


        # label = tk.Label(self, text = test_data['Questions'][])





>>>>>>> 16ce6beb21e96bacee5e1fe96a41a61fcb6a0672

        R1 = tk.Radiobutton(self, text="option 1", font=LARGE_FONT, indicatoron=0)
        R1.grid(row=2)
