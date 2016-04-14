import tkinter as tk
from StudentLogin import StudentLogin
from TeacherLogin import TeacherLogin
from tkinter import font

LARGE_FONT= ("Verdana", 12)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        
        label = tk.Label(self, text="Welcome to the Portal", font=self.headFont)
        label.pack(pady=10,padx=10)
        label.configure(background='white')

        button = tk.Button(self, text="I am a Student", font=self.titleFont, padx=5, pady=5, command=lambda: controller.show_frame(StudentLogin))
        button.configure(background = '#FF8800')
        button.pack()

        button2 = tk.Button(self, text="I am a Professor", font=self.titleFont, padx=5, pady=5, command=lambda: controller.show_frame(TeacherLogin))
        button2.configure(background = '#FF8800')
        button2.pack()
