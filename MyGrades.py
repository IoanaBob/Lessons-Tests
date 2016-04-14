import tkinter as tk

from MainStudentPage import *
import tkinter.messagebox as tm
import ast
import json




LARGE_FONT= ("Verdana", 12)

class MyGrades(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        tk.Frame.__init__(self, parent)
        
              
        
        
        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)        
        label = tk.Label(self, text="My Grades", font=self.headFont, padx=10, pady=10)
        label.grid(row=0, column=1)
        
        
        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))

        button1.grid(row=0, column=0)          
        
        
        
        enter_username_button = tk.Button(self, text="Generate Grades", font=self.buttonFont, padx=4, pady=4, command=lambda: self.stats(controller))
        enter_username_button.grid(row=3, column=1)
        
    def stats(self, controller):
        username = "username"

        with open('results.json') as data:
            json_decode = json.load(data)
        
        def test1results(controller, jsonfile):
            test1data = json_decode['username']['test1']
            test1data = ast.literal_eval(test1data)
            averagescore= sum(test1data)/len(test1data)
            topscore = max(test1data)
            
            return "\nScores for Test 1:", test1data, "\nAverage Score for Test 1:",averagescore,"\nTop Score for Test 1:",topscore
        
        def test2results(controller, jsonfile):
            test2data = json_decode['username']['test2']
            test2data = ast.literal_eval(test2data)
            averagescore= sum(test2data)/len(test2data)
            topscore = max(test2data)            
                       
            return "\n\nScores for Test 2:", test2data, "\nAverage Score for Test 2:",averagescore,"\nTop Score for Test 2:",topscore
            
        def bothresults(controller, jsonfile):
            test1results(controller, jsonfile)
            test2results(controller, jsonfile)
            
        for test1 in json_decode:
            if test1 == username:
                text = tk.Text(self)
                text.insert(tk.INSERT, test1results(controller, json_decode))
                text.insert(tk.INSERT, test2results(controller, json_decode))
                text.grid(row=5, column=1)
            else:
                tm.showerror("Username not found", "Username not found, please try again")        
        
        
        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
#        from ViewLesson1 import ViewLesson1
 #       from ViewLesson2 import ViewLesson2
  #      from TakeTest1 import TakeTest1
  #      from TakeTest2 import TakeTest2
  #      from StartPage import StartPage
  ##      from MyGrades import MyGrades
   #     #=====================================
   #     # MENU STARTS HERE
   #     # TODO: make buttons stay one near each other (not depending on the other columns)
   #     menu1 = tk.Button(self, text="Lesson 1", command=lambda: controller.show_frame(ViewLesson1))
   #     menu1.grid(row=0, column=0)
   #     menu2 = tk.Button(self, text="Lesson 2", command=lambda: controller.show_frame(ViewLesson2))
   #     menu2.grid(row=0, column=1)
   #     menu3 = tk.Button(self, text="Test 1", command=lambda: controller.show_frame(TakeTest1))
   ##     menu3.grid(row=0, column=2)
    #    menu4 = tk.Button(self, text="Test 2", command=lambda: controller.show_frame(TakeTest2))
    #    menu4.grid(row=0, column=3)
    #    menu5 = tk.Button(self, text="My Grades", command=lambda: controller.show_frame(MyGrades))
#        menu5.grid(row=0, column=4)
   ##     menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
    #    menu6.grid(row=0, column=5)
    #    #=====================================
#
#        label = tk.Label(self, text="All test results from user here", font=LARGE_FONT)
#        label.grid(row=1)
