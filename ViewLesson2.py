import tkinter as tk
from TakeTest2 import TakeTest2
LARGE_FONT= ("Verdana", 12)

class ViewLesson2(tk.Frame):

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
        menu5 = tk.Button(self, text="My Grades", command=lambda: controller.show_frame(ViewLesson2))
        menu5.grid(row=0, column=4)
        menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        menu6.grid(row=0, column=5)
        #=====================================

        label = tk.Label(self, text="{lesson 2 name}", font=LARGE_FONT)
        label.grid(row=1)

        text = tk.Text(self)
        text.insert(tk.INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pharetra libero lacus, vitae posuere neque placerat ut. Fusce imperdiet consequat justo quis maximus. Donec nec ligula elementum, placerat erat congue, feugiat nulla. Aenean vel dolor nibh. Donec tincidunt justo eget tellus suscipit accumsan. Cras sollicitudin convallis diam sit amet fringilla. Proin lacinia, metus eu aliquam accumsan, libero ligula convallis lectus, vitae volutpat quam lorem nec nulla. Donec sit amet sem eget ante accumsan sollicitudin lacinia eget orci. Sed ut pellentesque mauris. Mauris ac risus iaculis, aliquet elit id, sagittis ipsum. Pellentesque lobortis bibendum lorem eget gravida. In quis iaculis erat. Quisque vel mi varius, iaculis elit in, molestie magna. Nullam lacinia ante odio, vitae maximus sapien consequat et. Aliquam et ligula pretium, pretium felis ac, convallis sapien. Donec placerat dapibus ipsum, sit amet volutpat turpis efficitur eu.")

        text.insert(tk.END,"Morbi ac interdum odio. In nec turpis nisi. Vivamus efficitur sapien eu libero feugiat aliquam. Nunc eget justo vitae dolor egestas placerat sed id sem. Sed mollis felis non tortor accumsan, sit amet consectetur diam tristique. Pellentesque auctor est in lacus feugiat porttitor. Duis sit amet est quam. Proin tristique eu lacus eu vehicula.")

        text.insert(tk.END, "Fusce eget rhoncus justo. Pellentesque ut ipsum ac massa porta venenatis at malesuada orci. Suspendisse sollicitudin mollis aliquam. Sed nunc ligula, aliquet id massa et, tincidunt interdum lacus. Quisque at sodales eros, quis scelerisque nisl. Integer a justo nec justo ullamcorper tincidunt. Mauris eu enim aliquam sapien mollis vestibulum in at massa.")
        text.config(state=tk.DISABLED)
        text.grid(row=2)

        # Go to take test
        button1 = tk.Button(self, text="Take test", command=lambda: controller.show_frame(TakeTest2))
        button1.grid(row=3)

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons", command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=4)
