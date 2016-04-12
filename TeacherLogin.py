import tkinter as tk
from MainTeacherPage import *
import tkinter.messagebox as tm
import json


LARGE_FONT= ("Verdana", 12)

class TeacherLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # other pages imports
        from StartPage import StartPage

        label = tk.Label(self, text="Log In", font=LARGE_FONT)
        label.grid(row=0, column=1)

        # Adding the long in input fields
        self.number = tk.Label(self, text="Account:").grid(row=1)
        self.password = tk.Label(self, text="Password:").grid(row=2)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self, show="*")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        log_in_button = tk.Button(self, text="Log in", command=lambda: self.login(controller))
        log_in_button.grid(row=3, column=1)


        
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.grid(row=3, column=0)

    def login(self, controller):
        global username
        username = self.e1.get()
        password = self.e2.get()

        with open('users.json') as data_file:
            user_data = json.load(data_file)

        if user_data['Teachers'][username] == password:
            controller.show_frame(MainTeacherPage)
            return

        else:
            tm.showerror("Login Error", "Incorrect Username or pass")

