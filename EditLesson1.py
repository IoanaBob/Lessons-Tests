import tkinter as tk
import json
from TakeTest1 import TakeTest1

LARGE_FONT= ("Verdana", 12)

with open('lessons.json', 'r', encoding="utf-8") as data_file:
    lesson_data = json.load(data_file)

class EditLesson1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        label = tk.Label(self, text=lesson_data['Lessons'][0]['Lesson Title'], font=LARGE_FONT)
        label.grid(row=1)

        text = tk.Text(self)
        text.insert(tk.INSERT, lesson_data['Lessons'][0]['Lesson Content'])
        text.grid(row=2)

        save_button = tk.Button(self, text="Save Changes", command=lambda: save_changes() )
        save_button.grid(row=1)

        # Edit Test
        button1 = tk.Button(self, text="Edit test", command=lambda: controller.show_frame(EditTest1))
        button1.grid(row=3)

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons", command=lambda: controller.show_frame(MainTeacherPage))
        button2.grid(row=4)

        def save_changes():
            lesson_data['Lessons'][0]['Lesson Content'] = text.get("1.0", 'end-1c')

            with open(u"lessons.json", 'w', encoding="utf-8") as f:
                f.write(json.dumps(lesson_data))
