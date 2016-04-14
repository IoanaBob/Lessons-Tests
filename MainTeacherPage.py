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

        menu1 = tk.Button(self, text="Edit Probability Lesson", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(EditLesson1))
        menu1.grid(row=2, column=0)
        menu1.configure(background = '#FF8800')
        menu2 = tk.Button(self, text="Edit Sets Lesson",width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(EditLesson2))
        menu2.grid(row=2, column=2)
        menu2.configure(background = '#FF8800')
        menu3 = tk.Button(self, text="Modify Probability Test",width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(EditTest1))
        menu3.grid(row=4, column=0)
        menu3.configure(background = '#FF8800')
        menu4 = tk.Button(self, text="Modify Sets Test", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(EditTest2))
        menu4.grid(row=4, column=2)
        menu4.configure(background = '#FF8800')
        menu5 = tk.Button(self, text="View Statistics", width=20, font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(Statistics))
        menu5.grid(row=6, column=0, columnspan=3)
        menu5.configure(background = '#FF8800')
        menu6 = tk.Button(self, text="Log Out", font=self.buttonFont, padx=4, pady=4, relief=tk.RIDGE, command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=8, column=0, columnspan=3)
        #=====================================

        label = tk.Label(self, text="Welcome back.", font=self.headFont)
        label.grid(row=0, column=0, columnspan=2)
        label.configure(background = 'white')

        blank_space = tk.Label(self, text="")
        blank_space.configure(background = 'white')
        blank_space1 = tk.Label(self, text="")
        blank_space1.configure(background = 'white')
        blank_space2 = tk.Label(self, text="")
        blank_space2.configure(background = 'white')
        blank_space.grid(row=3, column = 1)
        blank_space1.grid(row=5, column = 1) 
        blank_space2.grid(row=7, column = 1)
