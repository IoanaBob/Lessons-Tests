import tkinter as tk
from TakeTest2 import TakeTest2
LARGE_FONT= ("Verdana", 12)

class ViewLesson2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="{lesson 2 name}", font=LARGE_FONT)
        label.grid(row=0)

        text = tk.Text(self)
        text.insert(tk.INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pharetra libero lacus, vitae posuere neque placerat ut. Fusce imperdiet consequat justo quis maximus. Donec nec ligula elementum, placerat erat congue, feugiat nulla. Aenean vel dolor nibh. Donec tincidunt justo eget tellus suscipit accumsan. Cras sollicitudin convallis diam sit amet fringilla. Proin lacinia, metus eu aliquam accumsan, libero ligula convallis lectus, vitae volutpat quam lorem nec nulla. Donec sit amet sem eget ante accumsan sollicitudin lacinia eget orci. Sed ut pellentesque mauris. Mauris ac risus iaculis, aliquet elit id, sagittis ipsum. Pellentesque lobortis bibendum lorem eget gravida. In quis iaculis erat. Quisque vel mi varius, iaculis elit in, molestie magna. Nullam lacinia ante odio, vitae maximus sapien consequat et. Aliquam et ligula pretium, pretium felis ac, convallis sapien. Donec placerat dapibus ipsum, sit amet volutpat turpis efficitur eu.")

        text.insert(tk.END,"Morbi ac interdum odio. In nec turpis nisi. Vivamus efficitur sapien eu libero feugiat aliquam. Nunc eget justo vitae dolor egestas placerat sed id sem. Sed mollis felis non tortor accumsan, sit amet consectetur diam tristique. Pellentesque auctor est in lacus feugiat porttitor. Duis sit amet est quam. Proin tristique eu lacus eu vehicula.")

        text.insert(tk.END, "Fusce eget rhoncus justo. Pellentesque ut ipsum ac massa porta venenatis at malesuada orci. Suspendisse sollicitudin mollis aliquam. Sed nunc ligula, aliquet id massa et, tincidunt interdum lacus. Quisque at sodales eros, quis scelerisque nisl. Integer a justo nec justo ullamcorper tincidunt. Mauris eu enim aliquam sapien mollis vestibulum in at massa.")
        text.config(state=tk.DISABLED)
        text.grid(row=1)
        
        # Go to take test
        button1 = tk.Button(self, text="Take test",
                            command=lambda: controller.show_frame(TakeTest2))
        button1.grid(row=2)

        from MainStudentPage import MainStudentPage
        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3)