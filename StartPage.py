import tkinter as tk
from StudentLogin import StudentLogin
from TeacherLogin import TeacherLogin


LARGE_FONT= ("Verdana", 12)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="I am a Student", command=lambda: controller.show_frame(StudentLogin))
        button.pack()

        button2 = tk.Button(self, text="I am a Professor", command=lambda: controller.show_frame(TeacherLogin))
        button2.pack()
