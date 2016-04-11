import tkinter as tk
from MainStudentPage import *

LARGE_FONT= ("Verdana", 12)

class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In!", font=LARGE_FONT)
        label.grid(row=0, column=1)

        # Adding the long in input fields
        number = tk.Label(self, text="Student number:").grid(row=1)
        password = tk.Label(self, text="Password:").grid(row=2)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        log_in_button = tk.Button(self, text="Log in", command=lambda: controller.show_frame(MainStudentPage))
        log_in_button.grid(row=3, column=1)



        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.grid(row=3, column=0)
