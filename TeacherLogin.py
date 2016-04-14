import tkinter as tk
from MainTeacherPage import *
import tkinter.messagebox as tm
import json


LARGE_FONT= ("Verdana", 12)

class TeacherLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        # other pages imports
        from StartPage import StartPage

        label = tk.Label(self, text="Log In", font=self.headFont)
        label.grid(row=0, column=1)
        label.configure(background = 'white')

        # Adding the long in input fields
        number = tk.Label(self, text="Account:", font=self.titleFont)
        number.grid(row=1, sticky="E")
        number.configure(background = 'white')
        password = tk.Label(self, text="Password:", font=self.titleFont)
        password.grid(row=2, sticky="E")
        password.configure(background = 'white')

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self, show="*")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        log_in_button = tk.Button(self, text="Log in", font=self.buttonFont, padx=4, pady=4, command=lambda: self.login(controller))
        log_in_button.configure(background = '#FF8800')
        log_in_button.grid(row=3, column=1)


        button1 = tk.Button(self, text="Back to Home",relief = tk.RIDGE, borderwidth = 4, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))

        button1.grid(row=0, column=0)

    def login(self, controller):
        global username
        username = self.e1.get()
        password = self.e2.get()

        with open('users.json', encoding="utf8") as data_file:
            user_data = json.load(data_file)
        try:
            user_data['Teachers'][username]
        except KeyError:
            tm.showerror("Login Error", "Incorrect Username or pass")
            return

        if user_data['Teachers'][username] == password:
            controller.show_frame(MainTeacherPage)
            return
        else:
            tm.showerror("Login Error", "Incorrect Username or pass")
