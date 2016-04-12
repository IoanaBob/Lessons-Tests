import tkinter as tk
import json
from random import randint

LARGE_FONT= ("Verdana", 12)

with open('questions.json') as data_file:
    test_data = json.load(data_file)

class TestPages(tk.Frame):

    def __init__(self, index, parent, controller):
        self.index = index
        
        tk.Frame.__init__(self, parent)

        # ============================================
        print(index)
        label = tk.Label(self, text=test_data['Questions'][index]['Question Header'], font=LARGE_FONT)
        label.grid(row=0)

        param = randint(0,len(test_data['Questions'][index]['Question Content'])-1)

        label = tk.Label(self, text=test_data['Questions'][index]['Question Content'][param]['Question'], font=LARGE_FONT)
        label.grid(row=1)

        answers = test_data['Questions'][index]['Question Content'][param]['Answers']
        j = 0
        for answer in answers:
            label = tk.Label(self, text=answer, font=LARGE_FONT)
            label.grid(row=2, column=j)
            j += 1

        print(index)
        if index < (len(test_data['Questions']) - 1):
            next = tk.Button(self, text="Lesson 1", command=lambda: controller.show_frame(TestPages(index+1, parent, controller)))
            next.grid(row=3, column=0)

