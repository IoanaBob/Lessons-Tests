import tkinter as tk
from tkinter import StringVar
import json
from random import randint
from tkinter import font

LARGE_FONT= ("Verdana", 12)

with open('questions2.json') as data_file:
    test_data = json.load(data_file)

class Test2Page3(tk.Frame):

    def __init__(self, parent, controller):
        from Test2Page4 import Test2Page4

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        def add_to_score(param):

            with open('current_score.json', 'r') as json_data:
                data = json.load(json_data)
            current_score = int(data["score"])

            if var.get() == test_data['Questions'][3]['Question Content'][param]['Correct Answer']:
                current_score += 1

            data = {"topic": 2, "score": current_score}
            with open('current_score.json', 'w') as json_data:
                json.dump(data, json_data)


        def combine_funcs(param):
            add_to_score(param)
            controller.refresh_frame(Test2Page4)
            controller.show_frame(Test2Page4)



        tk.Frame.__init__(self, parent)

        param = randint(0,len(test_data['Questions'][3]['Question Content'])-1)

        question = test_data['Questions'][3]['Question Header'] + test_data['Questions'][3]['Question Content'][param]['Question']
        label = tk.Label(self, text=question, font=self.titleFont, padx=4, pady=4)
        label.grid(row=1, sticky="W", columnspan=20)
        label.configure(background = 'white')

        answers = test_data['Questions'][3]['Question Content'][param]['Answers']
        j = 0
        var = StringVar()
        for answer in set(answers):
            radio = tk.Radiobutton(self, text=answer, font=self.textFont, relief = tk.SUNKEN, borderwidth = 4, width = 5, padx=4, pady=4, variable=var, value=answer)
            radio.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Next question", font=self.buttonFont, borderwidth = 4, padx=4, pady=4, command=lambda:combine_funcs(param))
        next.grid(row=3, column=0, columnspan=20, sticky="W")
        next.configure(background = '#FF8800')
