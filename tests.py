import tkinter as tk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StudentLogin, TeacherLogin, MainStudentPage, ViewLesson1, ViewLesson2, TakeTest1, TakeTest2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(column=0, row=0, sticky='nwes')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="I am a Student",
                            command=lambda: controller.show_frame(StudentLogin))
        button.pack()

        button2 = tk.Button(self, text="I am a Professor",
                            command=lambda: controller.show_frame(TeacherLogin))
        button2.pack()

###############################
# THE STUDENT FRAMES START HERE
class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In!", font=LARGE_FONT)
        label.grid(row=0)

        # Adding the long in input fields
        number = tk.Label(self, text="Student number:").grid(row=1)
        password = tk.Label(self, text="Password:").grid(row=2)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        ####################################
        # login button - goes to the lessons
        button1 = tk.Button(self, text="Log in",
                            command=lambda: controller.show_frame(MainStudentPage))
        button1.grid(row=3, column=1)

        # back to home button - will be deleted when menu will exist
        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=3, column=0)


class MainStudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello", font=LARGE_FONT)
        label.grid(row=0)
        # Go to view lesson1
        button1 = tk.Button(self, text="About {lesson 1}",
                            command=lambda: controller.show_frame(ViewLesson1))
        button1.grid(row=1, column=1)

        # Go to view test1
        button2 = tk.Button(self, text="About {lesson 2}",
                            command=lambda: controller.show_frame(ViewLesson2))
        button2.grid(row=2, column=1)

        # back to home button - will be deleted when menu will exist - also you cant go back if logged in
        button3 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1)

class ViewLesson1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="{lesson 1 name}", font=LARGE_FONT)
        label.grid(row=0)

        text = tk.Text(self)
        text.insert(tk.INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pharetra libero lacus, vitae posuere neque placerat ut. Fusce imperdiet consequat justo quis maximus. Donec nec ligula elementum, placerat erat congue, feugiat nulla. Aenean vel dolor nibh. Donec tincidunt justo eget tellus suscipit accumsan. Cras sollicitudin convallis diam sit amet fringilla. Proin lacinia, metus eu aliquam accumsan, libero ligula convallis lectus, vitae volutpat quam lorem nec nulla. Donec sit amet sem eget ante accumsan sollicitudin lacinia eget orci. Sed ut pellentesque mauris. Mauris ac risus iaculis, aliquet elit id, sagittis ipsum. Pellentesque lobortis bibendum lorem eget gravida. In quis iaculis erat. Quisque vel mi varius, iaculis elit in, molestie magna. Nullam lacinia ante odio, vitae maximus sapien consequat et. Aliquam et ligula pretium, pretium felis ac, convallis sapien. Donec placerat dapibus ipsum, sit amet volutpat turpis efficitur eu.")

        text.insert(tk.END,"Morbi ac interdum odio. In nec turpis nisi. Vivamus efficitur sapien eu libero feugiat aliquam. Nunc eget justo vitae dolor egestas placerat sed id sem. Sed mollis felis non tortor accumsan, sit amet consectetur diam tristique. Pellentesque auctor est in lacus feugiat porttitor. Duis sit amet est quam. Proin tristique eu lacus eu vehicula.")

        text.insert(tk.END, "Fusce eget rhoncus justo. Pellentesque ut ipsum ac massa porta venenatis at malesuada orci. Suspendisse sollicitudin mollis aliquam. Sed nunc ligula, aliquet id massa et, tincidunt interdum lacus. Quisque at sodales eros, quis scelerisque nisl. Integer a justo nec justo ullamcorper tincidunt. Mauris eu enim aliquam sapien mollis vestibulum in at massa.")
        text.config(state=tk.DISABLED)
        text.grid(row=1)
        
        # Go to take test
        button1 = tk.Button(self, text="Take test",
                            command=lambda: controller.show_frame(TakeTest1))
        button1.grid(row=2)

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3)

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

        # back to lessons
        button2 = tk.Button(self, text="Back to Lessons",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3)

class TakeTest1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MUST BE FINISHED - MUST HAVE A LOOP GOING THROUGH QUESTIONS ", font=LARGE_FONT)
        label.grid(row=0)

        # back to home button - will be deleted when menu will exist
        button2 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3, column=1)

class TakeTest2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MUST BE FINISHED - MUST HAVE A LOOP GOING THROUGH QUESTIONS ", font=LARGE_FONT)
        label.grid(row=0)

        # back to home button - will be deleted when menu will exist
        button2 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3, column=1)


###############################
# THE TEACHER FRAMES START HERE
# !!!TODO -  I WILL CONTINUE THAT LATER
class TeacherLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

# running the app
app = SeaofBTCapp()
app.mainloop()
