import tkinter as tk
from MainStudentPage import *
import tkinter.messagebox as tm
import json


LARGE_FONT= ("Verdana", 12)

class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In!", font=LARGE_FONT)
        label.grid(row=0, column=1)

        # Adding the long in input fields
        self.number = tk.Label(self, text="Student number:").grid(row=1)
        self.password = tk.Label(self, text="Password:").grid(row=2)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self, show="*")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        log_in_button = tk.Button(self, text="Log in", command=lambda: self.login())
        log_in_button.grid(row=3, column=1)

     
        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))

        button1.grid(row=3, column=0)
        
    def login(self):
        username = self.e1.get()
        password = self.e2.get() 


        my_data = json.loads(open("users.json").read())
        for key, value in my_data.items():
            for i in value:
                for key1, value1 in i.items():
                        
                    if username == key1 and password == value1:            
                        tm.showinfo("Login info", "HI")
                        # self.MainStudentPage()
                        return

                    else:
                        tm.showerror("Login error", "Incorrect username or password")    
                        return