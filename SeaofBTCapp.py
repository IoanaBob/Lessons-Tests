import tkinter as tk
from StartPage import StartPage
from StudentLogin import StudentLogin
from MainStudentPage import MainStudentPage
from ViewLesson1 import ViewLesson1
from ViewLesson2 import *
from TakeTest1 import *
from TakeTest2 import *
from TeacherLogin import TeacherLogin 



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

# running the app
app = SeaofBTCapp()
app.mainloop()

        


###############################
# THE STUDENT FRAMES START HERE


