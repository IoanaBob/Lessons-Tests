import tkinter as tk
from MainStudentPage import *

LARGE_FONT= ("Verdana", 12)

class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In!", font=LARGE_FONT)
        label.grid(row=0)

        # Adding the long in input fields
        number = tk.Label(self, text="Student number:").grid(row=1)
        password = tk.Label(self, text="Password:").grid(row=2)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        button1 = tk.Button(self, text="Log in",
                            command=lambda: controller.show_frame(MainStudentPage))
        button1.grid(row=3, column=1)

        from StartPage import StartPage
        # back to home button - will be deleted when menu will exist
        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=3, column=0)