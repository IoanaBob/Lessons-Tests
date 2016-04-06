import tkinter as tk
from ViewLesson1 import ViewLesson1
from ViewLesson2 import ViewLesson2

LARGE_FONT= ("Verdana", 12)

class MainStudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello", font=LARGE_FONT)
        label.grid(row=0)
        # Go to view lesson1
        button1 = tk.Button(self, text="About {lesson 1}",
                            command=lambda: controller.show_frame(ViewLesson1))
        button1.grid(row=1, column=1)

        # Go to view test1
        button2 = tk.Button(self, text="About {lesson 2}",
                            command=lambda: controller.show_frame(ViewLesson2))
        button2.grid(row=2, column=1)

        # back to home button - will be deleted when menu will exist - also you cant go back if logged in
        from StartPage import StartPage
        button3 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1)

