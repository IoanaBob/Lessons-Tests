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
        
        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", font=self.buttonFont, padx=4, pady=4, command=lambda: controller.show_frame(StartPage))

        button1.grid(row=0, column=0)          
        
        self.e1 = tk.Entry(self)
        
        self.e1.grid(row=1, column=1)
        
        enter_username_button = tk.Button(self, text="Enter", font=self.buttonFont, padx=4, pady=4, command=lambda: self.stats(controller))
        enter_username_button.grid(row=3, column=1)
        
    def stats(self, controller):
        global username_stats
        username_stats = self.e1.get()

        with open('results.json') as data:
            json_decode = json.load(data)
        
        def test1results(controller, jsonfile):
            for i in json_decode:
                if i == username_stats:                    
                    test1data = json_decode[i]['1']
                    #test1data = ast.literal_eval(test1data)
                    amountofscores = len(test1data)
                    sumofscores = sum(test1data)
                    if amountofscores == 0 or sumofscores == 0:
                        averagescore = "Can't divide by 0!"
                    else:
                        averagescore= sum(test1data)/len(test1data)
                    topscore = max(test1data)
                    #print("\nScores for Test 1:", test1data)    
                    #print("\nAverage Score for Test 1:",averagescore)
                    #print("\nTop Score for Test 1:",topscore)  
                    amountattempts = list(range(0,len(test1data)))    
                    plt.plot(amountattempts, test1data, 'ro')
                    plt.ylabel("Score")
                    plt.xlabel("Attempts")
                    plt.title('Test 1 Results')
                    plt.axis([-1,len(amountattempts)+1,0,10])
                    plt.show()
            return "\nScores for Test 1:", test1data, "\nAverage Score for Test 1:",averagescore,"\nTop Score for Test 1:",topscore
        
        def test2results(controller, jsonfile):
            for i in json_decode:
                if i == username_stats:
                    test2data = json_decode[i]['2']
                    #test2data = ast.literal_eval(test2data)
                    amountofscores = len(test2data)
                    sumofscores = sum(test2data)
                    if amountofscores == 0 or sumofscores == 0:
                        averagescore = "Can't divide by 0!"
                    else:
                        averagescore= sum(test2data)/len(test2data)
                        
                    topscore = max(test2data)            
                    #print("\nScores for Test 2:", test2data)    
                    #print("\nAverage Score for Test 2:",averagescore)
                    #print("\nTop Score for Test 2:",topscore)
                    amountattempts = list(range(0,len(test2data)))    
                    plt.plot(amountattempts, test2data, 'ro')
                    plt.ylabel("Score")
                    plt.xlabel("Attempts")
                    plt.title('Test 1 Results')
                    plt.axis([-1,len(amountattempts)+1,0,10])
                    plt.show()
            return "\n\nScores for Test 2:", test2data, "\nAverage Score for Test 2:",averagescore,"\nTop Score for Test 2:",topscore
            
        def bothresults(controller, jsonfile):
            test1results(controller, jsonfile)
            test2results(controller, jsonfile)
            
        #for test1 in json_decode:
            #if test1 == username_stats:
        text = tk.Text(self)
        text.insert(tk.INSERT, test1results(controller, json_decode))
        text.insert(tk.INSERT, test2results(controller, json_decode))
        text.grid(row=5, column=1)
           # else:
                #tm.showerror("Username not found", "Username not found, please try again")
        
        
        
        
        
        
    
#        # moved all the other page imports, makes it more clear and it works in any case.
#        # add more here, too, if you need to.
#        from EditLesson1 import EditLesson1
#        from EditLesson2 import EditLesson2
#        from TakeTest1 import TakeTest1
#        from TakeTest2 import TakeTest2
 ##       from EditTest1 import EditTest1
 #       from EditTest2 import EditTest2
 #       from Statistics import Statistics
 #       from StartPage import StartPage
  #      #=====================================
  ##      # MENU STARTS HERE
  #      TODO: make buttons stay one near each other (not depending on the other columns)
  #      menu1 = tk.Button(self, text="Edit Lesson 1", command=lambda: controller.show_frame(EditLesson1))
  #      menu1.grid(row=0, column=0)
  #      menu2 = tk.Button(self, text="Edit Lesson 2", command=lambda: controller.show_frame(EditLesson2))
  #      menu2.grid(row=0, column=1)
  #      menu3 = tk.Button(self, text="Modify Test 1", command=lambda: controller.show_frame(EditTest1))
   #     menu3.grid(row=0, column=2)
   #     menu4 = tk.Button(self, text="Modify Test 2", command=lambda: controller.show_frame(EditTest2))
  #      menu4.grid(row=0, column=3)
  #      menu5 = tk.Button(self, text="Statistics", command=lambda: controller.show_frame(Statistics))
  #      menu5.grid(row=0, column=4)
  #      menu6 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
  #      menu6.grid(row=0, column=5)
  #      #=====================================#

   #     label = tk.Label(self, text="MUST BE FINISHED", font=LARGE_FONT)
#        label.grid(row=1)
