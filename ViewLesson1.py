import tkinter as tk
import json
from TakeTest1 import TakeTest1

LARGE_FONT= ("Verdana", 12)

with open('lessons.json') as data_file:
    lesson_data = json.load(data_file)

class ViewLesson1(tk.Frame):

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=lesson_data['Lessons'][0]['Lesson Title'], font=LARGE_FONT)
        label.grid(row=0)

        text = tk.Text(self)
        text.insert(tk.INSERT, lesson_data['Lessons'][0]['Lesson Content'])


        # text.insert(tk.END," Morbi ac interdum odio. In nec turpis nisi. Vivamus efficitur sapien eu libero feugiat aliquam. Nunc eget justo vitae dolor egestas placerat sed id sem. Sed mollis felis non tortor accumsan, sit amet consectetur diam tristique. Pellentesque auctor est in lacus feugiat porttitor. Duis sit amet est quam. Proin tristique eu lacus eu vehicula.")
        # text.insert(tk.END, "Fusce eget rhoncus justo. Pellentesque ut ipsum ac massa porta venenatis at malesuada orci. Suspendisse sollicitudin mollis aliquam. Sed nunc ligula, aliquet id massa et, tincidunt interdum lacus. Quisque at sodales eros, quis scelerisque nisl. Integer a justo nec justo ullamcorper tincidunt. Mauris eu enim aliquam sapien mollis vestibulum in at massa.")
        text.config(state=tk.DISABLED)
        text.grid(row=1)

        # Go to take test
        button1 = tk.Button(self, text="Take test", command=lambda: controller.show_frame(TakeTest1))
        button1.grid(row=2)

        from MainStudentPage import MainStudentPage

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3)
