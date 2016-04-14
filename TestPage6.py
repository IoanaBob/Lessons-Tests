import tkinter as tk
from tkinter import StringVar
import json
from random import randint

LARGE_FONT= ("Verdana", 12)

with open('questions.json') as data_file:
    test_data = json.load(data_file)

class TestPage6(tk.Frame):

    def __init__(self, parent, controller):
        from MyGrades import MyGrades

        global current_score

        def add_to_score(param):

            with open('current_score.json', 'r') as json_data:
                data = json.load(json_data)
            global current_score
            current_score = int(data["score"])

            if var.get() == test_data['Questions'][6]['Question Content'][param]['Correct Answer']:
                current_score += 1

            print(current_score)

            data = {"topic": 1, "score": current_score}
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
                results[current_user]["1"].append(current_score)
            else:
                results[current_user] = {"1":[current_score],"2":[]}

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
        label = tk.Label(self, text=question, font=LARGE_FONT)
        label.grid(row=1)

        answers = test_data['Questions'][6]['Question Content'][param]['Answers']
        j = 0
        var = StringVar()
        for answer in set(answers):
            radio = tk.Radiobutton(self, text=answer, variable=var, value=answer)
            radio.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Done", command=lambda:combine_funcs(param))
        next.grid(row=3, column=0)
