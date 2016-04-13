import tkinter as tk
import json
from random import randint

LARGE_FONT= ("Verdana", 12)

with open('questions.json') as data_file:
    test_data = json.load(data_file)

class TestPage0(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        from TestPage1 import TestPage1
        # ============================================
        label = tk.Label(self, text=test_data['Questions'][0]['Question Header'], font=LARGE_FONT)
        label.grid(row=0)

        param = randint(0,len(test_data['Questions'][0]['Question Content'])-1)

        label = tk.Label(self, text=test_data['Questions'][0]['Question Content'][param]['Question'], font=LARGE_FONT)
        label.grid(row=1)

        answers = test_data['Questions'][0]['Question Content'][param]['Answers']
        j = 0
        for answer in answers:
            label = tk.Label(self, text=answer, font=LARGE_FONT)
            label.grid(row=2, column=j)
            j += 1

        next = tk.Button(self, text="Next question", command=lambda: controller.show_frame(TestPage1))
        next.grid(row=3, column=0)

