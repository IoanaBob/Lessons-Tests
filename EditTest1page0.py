import tkinter as tk
import json
from tkinter import font

with open('questions.json','r', encoding="utf-8") as data_file:
    questions = json.load(data_file)

LARGE_FONT= ("Verdana", 12)

class EditTest1Page0(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # moved all the other page imports, makes it more clear and it works in any case.
        # add more here, too, if you need to.
        from EditLesson1 import EditLesson1
        from EditLesson2 import EditLesson2
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

        label = tk.Label(self, text="Modify sets test", font=LARGE_FONT)
        label.grid(row=1)

        text = tk.Text(self)
        text.insert(tk.INSERT, questions["Questions"][0])
        text.grid(row=2)

        save_button = tk.Button(self, text="Save Changes", command=lambda: save_changes() )
        save_button.grid(row=3)

        # Next Question
        button1 = tk.Button(self, text="Edit test", command=lambda: controller.show_frame(EditTest1Page0))
        button1.grid(row=4)

        def save_changes():
            questions["Questions"][0] = text.get("1.0", 'end-1c')
            print(text.get("1.0", 'end-1c'))
            with open(u"questions.json", 'w', encoding="utf-8") as f:
                f.write(json.dumps(questions))

        '''
        topicl = tk.Label(self, text="Question Topic", font=LARGE_FONT)
        topicl.grid(row=2, column=0)

        topic = tk.Text(self, height=1, width= 40)
        topic.insert(tk.INSERT, questions['Questions'][0]['Question Topic'])
        topic.grid(row=2, column=1)
        #changing the dict
        questions['Questions'][0]['Question Topic'] = topic.get("1.0", 'end-1c')

        headerl = tk.Label(self, text="Question Header", font=LARGE_FONT)
        headerl.grid(row=3, column=0)

        header = tk.Text(self, height=1, width= 40)
        header.insert(tk.INSERT, questions['Questions'][0]['Question Header'])
        header.grid(row=3, column=1)
        #changing the dict
        questions['Questions'][0]['Question Header'] = header.get("1.0", 'end-1c')

        thecontent = tk.Label(self, text="Question Content - parameters", font=LARGE_FONT)
        thecontent.grid(row=4, column=0)

        j = 5
        i = 0
        content = []
        for question in questions['Questions'][0]['Question Content']:

            contentl = tk.Label(self, text="Parameter: ", font=LARGE_FONT)
            contentl.grid(row=j, column=0)
            content.append(tk.Text(self, height=1, width=40))
            content[i].insert(tk.INSERT, question["Question"])
            content[i].grid(row=j, column=1)
            content_button = tk.Button(self, text="Save", command=lambda: save_content(content,question,questions) )
            content_button.grid(row=j, column=2)


            canswerl = tk.Label(self, text="Correct answer:", font=LARGE_FONT)
            canswerl.grid(row=j+1, column=0)
            canswer = tk.Text(self, height=1, width= 40)
            canswer.insert(tk.INSERT, question["Correct Answer"])
            canswer.grid(row=j+1, column=1)
            #changing the dict
            question["Correct Answer"] = canswer.get("1.0", 'end-1c')

            answers = tk.Label(self, text="Answers", font=LARGE_FONT)
            answers.grid(row=j+2, column=0)

            k = 0
            for answer in question["Answers"]:
                the_answer = tk.Text(self, height=1, width= 10)
                the_answer.insert(tk.INSERT, answer)
                the_answer.grid(row=j+3, column=k)
                #changing the dict
                answer = the_answer.get("1.0", 'end-1c')
                k += 1
            j += 4
            i += 1

        save_button = tk.Button(self, text="Save Changes", command=lambda: save_changes() )
        save_button.grid(row=j)

        def save_content(content, questioni, questions):
            for question in questions['Questions'][0]['Question Content']:
                #changing the dict
                if questioni == question:
                    print(question)
                    print(questioni)
                    print(content.get("1.0", 'end-1c'))
                    question["Question"] = content.get("1.0", 'end-1c')
                    with open(u"questions.json", 'w', encoding="utf-8") as json_data:
                        json.dump(questions, json_data)
        '''










