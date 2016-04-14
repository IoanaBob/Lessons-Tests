import tkinter as tk
from MainStudentPage import *
import tkinter.messagebox as tm
import ast
import json
import matplotlib.pyplot as plt



LARGE_FONT= ("Verdana", 12)

class Statistics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.headFont = font.Font(family="Helvetica Neue Light", weight="normal", size=30)
        self.titleFont = font.Font(family="Helvetica Neue Light", weight="normal", size=20)
        self.buttonFont = font.Font(family="Helvetica Neue Light", weight="normal", size=18)        
        label = tk.Label(self, text="Search for Username", font=self.headFont, padx=10, pady=10)
        label.grid(row=0, column=1)
        self.username_stats = tk.Label(self, text="Username:", font=self.titleFont).grid(row=1, sticky="E")
        
        self.e1 = tk.Entry(self)
        
        self.e1.grid(row=1, column=1)
        
        enter_username_button = tk.Button(self, text="Enter", font=self.buttonFont, padx=4, pady=4, command=lambda: self.stats(username_stats))
        enter_username_button.grid(row=3, column=1)
        
    def stats(self, username_stats):
        global username_stats
        username_stats = self.e1.get()

        with open('results.json') as data:
            json_decode = json.load(data)
        
        def test1results(username_stats, jsonfile):
            test1data = json_decode['username']['test1']
            test1data = ast.literal_eval(test1data)
            averagescore= sum(test1data)/len(test1data)
            topscore = max(test1data)
            print("\nScores for Test 1:", test1data)    
            print("\nAverage Score for Test 1:",averagescore)
            print("\nTop Score for Test 1:",topscore)  
            amountattempts = list(range(0,len(test1data)))    
            plt.plot(amountattempts, test1data, 'ro')
            plt.ylabel("Score")
            plt.xlabel("Attempts")
            plt.axis([-1,len(amountattempts)+1,0,10])
            plt.show()
            return test1data
        
        def test2results(username_stats, jsonfile):
            test2data = json_decode['username']['test2']
            test2data = ast.literal_eval(test2data)
            averagescore= sum(test2data)/len(test2data)
            topscore = max(test2data)
            print("\nScores for Test 2:", test2data)    
            print("\nAverage Score for Test 2:",averagescore)
            print("\nTop Score for Test 2:",topscore)
            amountattempts = list(range(0,len(test2data)))    
            plt.plot(amountattempts, test2data, 'ro')
            plt.ylabel("Score")
            plt.xlabel("Attempts")
            plt.axis([-1,len(amountattempts)+1,0,10])
            plt.show()
            return test2data
            
        def bothresults(username_stats, jsonfile):
            test1results(username_stats, jsonfile)
            test2results(username_stats, jsonfile)
            
        for test1 in json_decode:
            if test1 == username_stats:
                bothresults(username_stats,json_decode)
            else:
                tm.showerror("Username not found")
        
        
        
        text = tk.Text(self)
        text.insert(tk.INSERT, bothresults(username_stats, json_decode))
        
        text.config(state=tk.DISABLED)
        text.grid(row=2)
        
        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from EditLesson1 import EditLesson1
        from EditLesson2 import EditLesson2
        from TakeTest1 import TakeTest1
        from TakeTest2 import TakeTest2
        from EditTest1 import EditTest1
        from EditTest2 import EditTest2
        from Statistics import Statistics
        from StartPage import StartPage
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

        label = tk.Label(self, text="MUST BE FINISHED", font=LARGE_FONT)
        label.grid(row=1)
