import tkinter as tk
LARGE_FONT= ("Verdana", 12)

class TakeTest1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MUST BE FINISHED - MUST HAVE A LOOP GOING THROUGH QUESTIONS ", font=LARGE_FONT)
        label.grid(row=0)

        from MainStudentPage import MainStudentPage

        # back to home button - will be deleted when menu will exist
        button2 = tk.Button(self, text="Home", command=lambda: controller.show_frame(MainStudentPage))
        button2.grid(row=3, column=1)
