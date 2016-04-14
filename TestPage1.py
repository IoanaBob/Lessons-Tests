import tkinter as tk
from tkinter import StringVar
import json
from random import randint

LARGE_FONT= ("Verdana", 12)

with open('questions.json', encoding="utf-8") as data_file:
    test_data = json.load(data_file)

class TestPage1(tk.Frame):

    def __init__(self, parent, controller):
        from TestPage2 import TestPage2

        def add_to_score(param):

            with open('current_score.json', 'r') as json_data:
                data = json.load(json_data)
            current_score = int(data["score"])

            if var.get() == test_data['Questions'][1]['Question Content'][param]['Correct Answer']:
                current_score += 1


            data = {"topic": 1, "score": current_score}
            with open('current_score.json', 'w') as json_data:
                json.dump(data, json_data)


        def combine_funcs(param):
            add_to_score(param)
            controller.refresh_frame(TestPage2)
            controller.show_frame(TestPage2)



        tk.Frame.__init__(self, parent)

        param = randint(0,len(test_data['Questions'][1]['Question Content'])-1)

        question = test_data['Questions'][1]['Question Header'] + test_data['Questions'][1]['Question Content'][param]['Question']
        label = tk.Label(self, text=question, font=LARGE_FONT)
        label.grid(row=1)

        answers = test_data['Questions'][1]['Question Content'][param]['Answers']
        j = 0
        var = StringVar()
        for answer in set(answers):
            radio = tk.Radiobutton(self, text=answer, variable=var, value=answer)
            radio.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Next question", command=lambda:combine_funcs(param))
        next.grid(row=3, column=0)
