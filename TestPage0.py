import tkinter as tk
from tkinter import StringVar
import json
from random import randint

LARGE_FONT= ("Verdana", 12)

with open('questions.json') as data_file:
    test_data = json.load(data_file)

class TestPage0(tk.Frame):

    def __init__(self, parent, controller):
        from TestPage1 import TestPage1
        # ============================================
        # this variable will store the scores for a test taken by a student
        global total_score
        total_score = 0
        # ============================================

        def sel():
            if var.get() == 1:
                selection = "You are right!"
            else:
                selection = "You are not right. here is the explanation: \n blablabla"

        def add_to_score(param):
            global total_score
            if var.get() == test_data['Questions'][0]['Question Content'][param]['Correct Answer']:
                total_score += 1
        
        def combine_funcs(param):
            add_to_score(param)
            print(total_score)
            controller.show_frame(TestPage1)



        tk.Frame.__init__(self, parent)

        
        label = tk.Label(self, text=test_data['Questions'][0]['Question Header'], font=LARGE_FONT)
        label.grid(row=0)

        param = randint(0,len(test_data['Questions'][0]['Question Content'])-1)

        label = tk.Label(self, text=test_data['Questions'][0]['Question Content'][param]['Question'], font=LARGE_FONT)
        label.grid(row=1)

        answers = test_data['Questions'][0]['Question Content'][param]['Answers']
        j = 0
        var = StringVar()
        for answer in set(answers):
            radio = tk.Radiobutton(self, text=answer, variable=var, value=answer)
            radio.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Next question", command=lambda:combine_funcs(param))
        next.grid(row=3, column=0)

    

