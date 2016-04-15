import tkinter as tk
import json
from tkinter import font

with open('questions.json','r', encoding="utf-8") as data_file:
    questions = json.load(data_file)

LARGE_FONT= ("Verdana", 12)

class EditTest1Page6(tk.Frame):

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
        from EditTest1Page0 import EditTest1Page0
        from EditTest1Page1 import EditTest1Page1
        from EditTest1Page2 import EditTest1Page2
        from EditTest1Page3 import EditTest1Page3
        from EditTest1Page4 import EditTest1Page4
        from EditTest1Page5 import EditTest1Page5
        from EditTest1Page6 import EditTest1Page6
        from MainTeacherPage import MainTeacherPage
        #=====================================

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)

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
        # 2nd menu
        q0 = tk.Button(self, text="Question 1", command=lambda: controller.show_frame(EditTest1Page0))
        q0.grid(row=1, column=0)
        q1 = tk.Button(self, text="Question 2", command=lambda: controller.show_frame(EditTest1Page1))
        q1.grid(row=1, column=1)
        q2 = tk.Button(self, text="Question 3", command=lambda: controller.show_frame(EditTest1Page2))
        q2.grid(row=1, column=2)
        q3 = tk.Button(self, text="Question 4", command=lambda: controller.show_frame(EditTest1Page3))
        q3.grid(row=1, column=3)
        q4 = tk.Button(self, text="Question 5", command=lambda: controller.show_frame(EditTest1Page4))
        q4.grid(row=1, column=4)
        q5 = tk.Button(self, text="Question 6", command=lambda: controller.show_frame(EditTest1Page5))
        q5.grid(row=1, column=5)
        q6 = tk.Button(self, text="Question 7", command=lambda: controller.show_frame(EditTest1Page6))
        q6.grid(row=1, column=6)
        # =====================================

        label = tk.Label(self, text="Modify sets test", font=LARGE_FONT)
        label.grid(row=2)

        text = tk.Text(self)
        text.insert(tk.INSERT, questions["Questions"][6])
        text.grid(row=3)

        save_button = tk.Button(self, text="Save Changes", command=lambda: save_changes() )
        save_button.grid(row=4)


        def save_changes():
            questions["Questions"][6] = text.get("1.0", 'end-1c')
            print(text.get("1.0", 'end-1c'))
            with open(u"questions.json", 'w', encoding="utf-8") as f:
                f.write(json.dumps(questions))
