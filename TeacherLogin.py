import tkinter as tk


LARGE_FONT= ("Verdana", 12)

###############################
# THE TEACHER FRAMES START HERE
# !!!TODO -  I WILL CONTINUE THAT LATER
class TeacherLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        from StartPage import StartPage

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
