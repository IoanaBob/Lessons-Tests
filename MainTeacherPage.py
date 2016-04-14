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

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

        menu1 = tk.Button(self, text="Edit Probability Lesson", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditLesson1))
        menu1.grid(row=1, column=0)
        menu2 = tk.Button(self, text="Edit Sets Lesson", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditLesson2))
        menu2.grid(row=1, column=1)
        menu3 = tk.Button(self, text="Modify Probability Test", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditTest1))
        menu3.grid(row=2, column=0)
        menu4 = tk.Button(self, text="Modify Sets Test", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditTest2))
        menu4.grid(row=2, column=1)
        menu5 = tk.Button(self, text="View Statistics", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(Statistics))
        menu5.grid(row=3, column=0, columnspan=2)
        menu6 = tk.Button(self, text="Log Out", width=17, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=5, column=0, columnspan=2)
        #=====================================

        label = tk.Label(self, text="Welcome back.", font=self.headFont)
        label.grid(row=0, column=0, columnspan=2)

        blank_space = tk.Label(self, text="")
        blank_space.grid(row=4, column=0, columnspan=2)
