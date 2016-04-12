import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class MainStudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from ViewLesson1 import ViewLesson1
        from ViewLesson2 import ViewLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from StartPage import StartPage
        from MyGrades import MyGrades
        #=====================================
        # MENU STARTS HERE
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu1 = tk.Button(self, text="Lesson 1", command=lambda: controller.show_frame(ViewLesson1))
        menu1.grid(row=0, column=0)
        menu2 = tk.Button(self, text="Lesson 2", command=lambda: controller.show_frame(ViewLesson2))
        menu2.grid(row=0, column=1)
        menu3 = tk.Button(self, text="Test 1", command=lambda: controller.show_frame(TakeTest1))
        menu3.grid(row=0, column=2)
        menu4 = tk.Button(self, text="Test 2", command=lambda: controller.show_frame(TakeTest2))
        menu4.grid(row=0, column=3)
        menu5 = tk.Button(self, text="My Grades", command=lambda: controller.show_frame(MyGrades))
        menu5.grid(row=0, column=4)
        menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=0, column=5)
        #=====================================

        label = tk.Label(self, text="Hello", font=LARGE_FONT)
        label.grid(row=1)
        # Go to view lesson1
        button1 = tk.Button(self, text="About {lesson 1}", command=lambda: controller.show_frame(ViewLesson1))
        button1.grid(row=2, column=1)

        # Go to view test1
        button2 = tk.Button(self, text="About {lesson 2}", command=lambda: controller.show_frame(ViewLesson2))
        button2.grid(row=3, column=1)

        # back to home button - will be deleted when menu will exist - also you cant go back if logged in       button3 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button3 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button3.grid(row=4, column=1)
