import tkinter as tk
from tkinter import font
LARGE_FONT= ("Verdana", 12)

class EditTest1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from EditLesson1 import EditLesson1
        from EditLesson2 import EditLesson2
        from EditTest1 import EditTest1
        from EditTest2 import EditTest2
        from Statistics import Statistics
        from StartPage import StartPage
        #=====================================
        from EditTest1page0 import EditTest1Page0
        #=====================================

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        # MENU STARTS HERE
        # TODO: make buttons stay one near each other (not depending on the other columns)
        menu1 = tk.Button(self, text="Edit Probability Lesson",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditLesson1))
        menu1.grid(row=0, column=0)
        menu1.configure(background = '#FF8800')
        menu2 = tk.Button(self, text="Edit Sets Lesson",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditLesson2))
        menu2.grid(row=0, column=1)
        menu2.configure(background = '#FF8800')
        menu3 = tk.Button(self, text="Modify Probability Test",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditTest1))
        menu3.grid(row=0, column=2)
        menu3.configure(background = '#FF8800')
        menu4 = tk.Button(self, text="Modify Sets Test",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditTest2))
        menu4.grid(row=0, column=3)
        menu4.configure(background = '#FF8800')
        menu5 = tk.Button(self, text="Statistics",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(Statistics))
        menu5.grid(row=0, column=4)
        menu5.configure(background = '#FF8800')
        menu6 = tk.Button(self, text="Log Out",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=0, column=6)
        menu6.configure(background = '#FF8800')
        menu7 = tk.Button(self, text="Back Home",  padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(MainTeacherPage))
        menu7.grid(row=0, column=5)
        menu7.configure(background = '#FF8800')
        #=====================================

        q0 = tk.Button(self, text="Question 1", command=lambda: controller.show_frame(EditTest1Page0))
        q0.grid(row=1, column=0)
        q1 = tk.Button(self, text="Question 2", command=lambda: controller.show_frame(EditTest1Page0))
        q1.grid(row=1, column=1)
        q2 = tk.Button(self, text="Question 3", command=lambda: controller.show_frame(EditTest1Page0))
        q2.grid(row=1, column=2)
        q3 = tk.Button(self, text="Question 4", command=lambda: controller.show_frame(EditTest1Page0))
        q3.grid(row=1, column=3)
        q4 = tk.Button(self, text="Question 5", command=lambda: controller.show_frame(EditTest1Page0))
        q4.grid(row=1, column=4)
        q5 = tk.Button(self, text="Question 6", command=lambda: controller.show_frame(EditTest1Page0))
        q5.grid(row=1, column=5)
        q6 = tk.Button(self, text="Question 7", command=lambda: controller.show_frame(EditTest1Page0))
        q6.grid(row=1, column=6)
