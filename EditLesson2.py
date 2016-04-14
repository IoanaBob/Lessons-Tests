import tkinter as tk
import json
from TakeTest2 import TakeTest2
from tkinter import font

# SETS

LARGE_FONT= ("Verdana", 20)

with open('lessons.json', 'r', encoding="utf-8") as data_file:
    lesson_data = json.load(data_file)

class EditLesson2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)
        self.textFont = font.Font(family="Helvetica Neue Light", weight="normal", size=12)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from EditLesson1 import EditLesson1
        from EditLesson2 import EditLesson2
        from EditTest1 import EditTest1
        from EditTest2 import EditTest2
        from StartPage import StartPage
        from MainTeacherPage import MainTeacherPage
        from Statistics import Statistics
        #=====================================
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

        label = tk.Label(self,  text=lesson_data['Lessons'][1]['Lesson Title'], font=self.headFont)
        label.grid(row=1)
        label.configure( background = 'white')

        text = tk.Text(self)
        text.insert(tk.INSERT, lesson_data['Lessons'][1]['Lesson Content'])
        text.grid(row=3, column=0, columnspan=20, sticky="W")
        # =================================
        # TODO - when modified, the new text in the textbox is saved in te JSON
        # A SAVE BUTTON IS NEEDED HERE
        # =================================

        save_button = tk.Button(self, text="Save Changes", font=self.buttonFont, pady=4, padx=4, command=lambda: save_changes() )
        save_button.grid(row=4, column=0)

        # Edit Test
        button1 = tk.Button(self, text="Edit Test", borderwidth = 4, padx=4, pady=4, font=self.buttonFont, command=lambda: controller.show_frame(EditTest1))
        button1.grid(row=4, column=1)
        button1.configure(background = '#FF8800')

        def save_changes():
            lesson_data['Lessons'][1]['Lesson Content'] = text.get("1.0", 'end-1c')

            with open(u"lessons.json", 'w', encoding="utf-8") as f:
                f.write(json.dumps(lesson_data))
