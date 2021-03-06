import tkinter as tk
from MainStudentPage import *
import tkinter.messagebox as tm
import json

LARGE_FONT= ("Verdana", 12)

class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        label = tk.Label(self, text="Log In", font=self.headFont, padx=10, pady=10)
        label.grid(row=0, column=1)
        label.configure(background = 'white')

        # Adding the long in input fields
        number = tk.Label(self, text="Student number:", font=self.titleFont)
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
        log_in_button = tk.Button(self, text="Log in", borderwidth = 4, font=self.buttonFont, padx=4, pady=4, command=lambda: self.login(controller, parent))
        log_in_button.grid(row=3, column=1)
        log_in_button.configure(background = '#FF8800')


        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home",relief = tk.RIDGE, borderwidth = 4, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))

        button1.grid(row=0, column=0)

    def login(self, controller, parent):
        global username
        username = self.e1.get()
        password = self.e2.get()

        with open('users.json', encoding="utf-8") as data_file:
            user_data = json.load(data_file)

        try:
            user_data['Students'][username]
        except KeyError:
            tm.showerror("Login Error", "Incorrect Username or pass")
            return
        if user_data['Students'][username] == password:
            # adding current user info
            data = {"username": username, "student": True}
            with open('current_user.json', 'w') as json_data:
                json.dump(data, json_data)
       
            # ========================
            controller.refresh_frame(MainStudentPage)
            controller.show_frame(MainStudentPage)
            return

        else:
            tm.showerror("Login Error", "Incorrect Username or pass")
