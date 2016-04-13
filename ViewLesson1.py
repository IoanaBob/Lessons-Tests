import tkinter as tk
import json
from TakeTest1 import TakeTest1

LARGE_FONT= ("Verdana", 12)

with open('lessons.json') as data_file:
    lesson_data = json.load(data_file)

class ViewLesson1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from ViewLesson1 import ViewLesson1
        from ViewLesson2 import ViewLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from StartPage import StartPage
        from MainStudentPage import MainStudentPage
        from MyGrades import MyGrades
        # from TestPages import TestPages
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

        label = tk.Label(self, text=lesson_data['Lessons'][0]['Lesson Title'], font=LARGE_FONT)
        label.grid(row=1)

        text = tk.Text(self)
        text.insert(tk.INSERT, lesson_data['Lessons'][0]['Lesson Content'])


        # text.insert(tk.END," Morbi ac interdum odio. In nec turpis nisi. Vivamus efficitur sapien eu libero feugiat aliquam. Nunc eget justo vitae dolor egestas placerat sed id sem. Sed mollis felis non tortor accumsan, sit amet consectetur diam tristique. Pellentesque auctor est in lacus feugiat porttitor. Duis sit amet est quam. Proin tristique eu lacus eu vehicula.")
        # text.insert(tk.END, "Fusce eget rhoncus justo. Pellentesque ut ipsum ac massa porta venenatis at malesuada orci. Suspendisse sollicitudin mollis aliquam. Sed nunc ligula, aliquet id massa et, tincidunt interdum lacus. Quisque at sodales eros, quis scelerisque nisl. Integer a justo nec justo ullamcorper tincidunt. Mauris eu enim aliquam sapien mollis vestibulum in at massa.")
        text.config(state=tk.DISABLED)
        text.grid(row=2)

        # Go to take test
        button1 = tk.Button(self, text="Take test", command=lambda: controller.show_frame(TakeTest1))
        button1.grid(row=3)

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=4)
