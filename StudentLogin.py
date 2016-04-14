import tkinter as tk
from MainStudentPage import *
import tkinter.messagebox as tm
import json

username = ""
LARGE_FONT= ("Verdana", 12)

class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        label = tk.Label(self, text="Log In", font=self.headFont, padx=10, pady=10)
        label.grid(row=0, column=1)

        # Adding the long in input fields
        self.number = tk.Label(self, text="Student number:", font=self.titleFont).grid(row=1, sticky="E")
        self.password = tk.Label(self, text="Password:", font=self.titleFont).grid(row=2, sticky="E")

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self, show="*")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        log_in_button = tk.Button(self, text="Log in", font=self.buttonFont, padx=4, pady=4, command=lambda: self.login(controller))
        log_in_button.grid(row=3, column=1)


        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))

        button1.grid(row=0, column=0)

    def login(self, controller):
        global username
        username = self.e1.get()
        print(username)
        password = self.e2.get()

        with open('users.json') as data_file:
            user_data = json.load(data_file)

        try:
            user_data['Students'][username]
        except KeyError:
            tm.showerror("Login Error", "Incorrect Username or pass")
            return
        if user_data['Students'][username] == password:
            controller.show_frame(MainStudentPage)
            return

        else:
            tm.showerror("Login Error", "Incorrect Username or pass")
