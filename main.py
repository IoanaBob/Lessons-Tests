import tkinter as tk
from StartPage import StartPage
from StudentLogin import StudentLogin
from MainStudentPage import MainStudentPage
from MainTeacherPage import MainTeacherPage
from ViewLesson1 import ViewLesson1
from ViewLesson2 import ViewLesson2
from EditLesson1 import EditLesson1
from EditLesson2 import EditLesson2
from TakeTest1 import *
from TakeTest2 import *
from EditTest1 import EditTest1
from EditTest2 import EditTest2
from Statistics import Statistics
from MyGrades import MyGrades
from TeacherLogin import TeacherLogin
from TestPages import TestPages


LARGE_FONT= ("Verdana", 12)


class main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StudentLogin, TeacherLogin, MainStudentPage, MainTeacherPage, ViewLesson1, ViewLesson2,
            EditLesson1, EditLesson2, TakeTest1, TakeTest2, EditTest1, EditTest2, MyGrades, Statistics):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(column=0, row=0, sticky='nwes')

        for i in range(0,1):
            frame = TestPages(i, container, self)

            self.frames[TestPages] = frame

            frame.grid(column=0, row=0, sticky='nwes')

        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# running the app
app = main()
app.mainloop()
