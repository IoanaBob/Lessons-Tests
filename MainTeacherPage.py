import tkinter as tk
from tkinter import font

LARGE_FONT= ("Verdana", 12)

class MainTeacherPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from EditLesson1 import EditLesson1
        from EditLesson2 import EditLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from EditTest1 import EditTest1
        from EditTest2 import EditTest2
        from Statistics import Statistics
        from StartPage import StartPage
        #=====================================
        # MENU STARTS HERE
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu1 = tk.Button(self, text="Edit Lesson 1", command=lambda: controller.show_frame(EditLesson1))
        menu1.grid(row=0, column=0)
        menu2 = tk.Button(self, text="Edit Lesson 2", command=lambda: controller.show_frame(EditLesson2))
        menu2.grid(row=0, column=1)
        menu3 = tk.Button(self, text="Modify Test 1", command=lambda: controller.show_frame(EditTest1))
        menu3.grid(row=0, column=2)
        menu4 = tk.Button(self, text="Modify Test 2", command=lambda: controller.show_frame(EditTest2))
        menu4.grid(row=0, column=3)
        menu5 = tk.Button(self, text="Statistics", command=lambda: controller.show_frame(Statistics))
        menu5.grid(row=0, column=4)
        menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=0, column=5)
        #=====================================

        label = tk.Label(self, text="Hello", font=LARGE_FONT)
        label.grid(row=1)
        # Go to view lesson1
        button1 = tk.Button(self, text="Edit Lesson 1", command=lambda: controller.show_frame(EditLesson1))
        button1.grid(row=2, column=1)

        # Go to view test1
        button2 = tk.Button(self, text="Edit Lesson 2", command=lambda: controller.show_frame(EditLesson2))
        button2.grid(row=3, column=1)

        # back to home button - will be deleted when menu will exist - also you cant go back if logged in       button3 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button3 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button3.grid(row=4, column=1)
