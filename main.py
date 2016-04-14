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
from TestPage0 import TestPage0
from TestPage1 import TestPage1
from TestPage2 import TestPage2
from TestPage3 import TestPage3
from TestPage4 import TestPage4
from TestPage5 import TestPage5
from TestPage6 import TestPage6
from Test2Page0 import Test2Page0
from Test2Page1 import Test2Page1
from Test2Page2 import Test2Page2
from Test2Page3 import Test2Page3
from Test2Page4 import Test2Page4
from Test2Page5 import Test2Page5
from Test2Page6 import Test2Page6


from EditTest1Page0 import EditTest1Page0


LARGE_FONT= ("Verdana", 12)


class main(tk.Tk):
 
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        for F in (StartPage, StudentLogin, TeacherLogin, MainStudentPage, MainTeacherPage, ViewLesson1, ViewLesson2, 
            EditLesson1, EditLesson2, TakeTest1, TakeTest2, EditTest1, EditTest2, MyGrades, 
            Statistics, TestPage1, TestPage0, TestPage2, TestPage3, TestPage4, TestPage5, TestPage6,Test2Page0, Test2Page1,Test2Page2,Test2Page3, Test2Page4,
            Test2Page5,Test2Page6,EditTest1Page0):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(column=0, row=0, sticky='nwes')

        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.configure(background='white')
        frame.tkraise()


    def refresh_frame(self, F):
        self.frames[F].destroy()
        frame = F(self.container, self)
        self.frames[F] = frame
        frame.grid(column=0, row=0, sticky='nwes')

def end_session(root):
    root.destroy()

# running the app
app = main()
app.mainloop()
