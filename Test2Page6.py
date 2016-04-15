import tkinter as tk
from tkinter import StringVar
import json
from random import randint
from tkinter import font

LARGE_FONT= ("Verdana", 12)

with open('questions2.json') as data_file:
    test_data = json.load(data_file)

class Test2Page6(tk.Frame):

    def __init__(self, parent, controller):
        from MyGrades import MyGrades

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        global current_score

        def add_to_score(param):

            with open('current_score.json', 'r') as json_data:
                data = json.load(json_data)
            global current_score
            current_score = int(data["score"])

            if var.get() == test_data['Questions'][6]['Question Content'][param]['Correct Answer']:
                current_score += 1

            print(current_score)

            data = {"topic": 2, "score": current_score}
            with open('current_score.json', 'w') as json_data:
                json.dump(data, json_data)

        def add_to_results():
            global current_score
            with open('current_user.json', 'r') as json_data:
                user = json.load(json_data)
            current_user = user["username"]

            with open('results.json', 'r') as json_data:
                results = json.load(json_data)
            if current_user in results:
                results[current_user]["2"].append(current_score)
            else:
                results[current_user] = {"1":[],"2":[current_score]}

            with open('results.json', 'w') as json_data:
                json.dump(results, json_data)


        def combine_funcs(param):
            add_to_score(param)
            add_to_results()
            controller.refresh_frame(MyGrades)
            controller.show_frame(MyGrades)



        tk.Frame.__init__(self, parent)

        param = randint(0,len(test_data['Questions'][6]['Question Content'])-1)

        question = test_data['Questions'][6]['Question Header'] + test_data['Questions'][6]['Question Content'][param]['Question']
        label = tk.Label(self, text=question, font=self.titleFont, padx=4, pady=4)
        label.grid(row=1, sticky="W", columnspan=20)

        label.configure(background = 'white')

        answers = test_data['Questions'][6]['Question Content'][param]['Answers']
        j = 0
        var = StringVar()
        for answer in set(answers):
            radio = tk.Radiobutton(self, text=answer, font=self.textFont, relief = tk.SUNKEN, borderwidth = 4,  padx=4, pady=4, variable=var, value=answer)
            radio.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Submit Test", font=self.buttonFont, borderwidth = 4, padx=4, pady=4, command=lambda:combine_funcs(param))
        next.grid(row=3, column=0, columnspan=20, sticky="W")
        next.configure(background = '#FF8800')
