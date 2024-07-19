from tkinter import *
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.questions = [
            {"question":"capital of France?","options":["Paris","London","Jupiter","Baguette"],"answer":"Paris"},
            {"question":"1+1","options":["4","2","window","11"],"answer":"2"},
            {"question":"color of sky","options":["Orange","Purple","Green","Blue"],"answer":"Blue"},
            {"question":"what is a metallic minieral","options":["potash","copper","marble","salt"],"answer":"copper"},
            {"question":"what color is a Lotus","options":["What is a lotus?","Blue","Pink","Black"],"answer":"Pink"},
            {"question":"what was the first question?","options":["capital of France","color of the sky","1+1","I give up"],"answer":"capital of France"}
        ]
        self.score = 0
        self.current_question = 0

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score = self.score + 1
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.current_question + 1
        if self.current_question < len(self.questions):
            return True
        else:
            return False

class App(Tk):
    def __init__(self, quiz):
        Tk.__init__(self)
        self.title("Quiz")  #  The name of the application
        self.my_quiz = quiz
        self.config(bg="lightblue")
        self.geometry("600x400")
        # Title
        self.title = Label(self,text="Quiz Time")
        self.title.config(font=("Courier",15))
        self.title.pack(pady=10)
        #  Question Label
        self.question_label = Label(self,text="",wraplength=400)
        self.question_label.config(font=("Arial",12))
        self.question_label.pack(pady=20)
        # List of options
        self.option_list = StringVar(value="")
        self.option_button = []

        for i in range(4): # all codes under will run twice
            rb = Radiobutton(self,text="",variable=self.option_list,value="")
            rb.pack(anchor=W,padx=200,pady=5)
            self.option_button.append(rb)
        # submit Button
        self.submit_button = Button(self,text="Submit",command=self.submit_answer)
        self.submit_button.config(font=("Arial",12))
        self.submit_button.pack(pady=20)
        #  Answer Label
        self.answer_label = Label(self,text="")
        self.answer_label.config(font=("Courier",12))
        self.answer_label.pack(pady=20)
        #  Score Label
        self.score_label = Label(self,text="Score: 0")
        self.score_label.config(font=("Courier",12))
        self.score_label.pack(pady=10)
        self.load_question()

    def load_question(self):
        question_data =self.my_quiz.questions[self.my_quiz.current_question] # dictionary of the current question
        self.question_label.config(text=question_data["question"])  #  set the question text
        self.option_list.set("")  # set the default value for options

        for index,option in enumerate(question_data["options"]):
            self.option_button[index].config(text=option, value=option)

    def submit_answer(self):
        # read the current option
        # use check_answer function to check answer
        # go to next question / show score
        selected_option = self.option_list.get()
        correct = self.my_quiz.check_answer(selected_option)  #  True/False?
        if correct:
            self.answer_label.config(text="Correct", fg="green")
        else:
            correct_answer = self.my_quiz.questions[self.my_quiz.current_question]["answer"]
            self.answer_label.config(text=f"Wrong! Correct Answer:{correct_answer}", fg="red")

        self.score_label.config(text=f"Score: {self.my_quiz.score}")

        if self.my_quiz.next_question():
            self.load_question()
        else:
            self.end_quiz()


    def end_quiz(self):
        number_of_questions = len(self.my_quiz.questions)
        messagebox.showinfo("Quiz Completed",f"Your Score: {self.my_quiz.score}/{number_of_questions}")
        self.submit_button.config(state=DISABLED)

# launch App
my_quiz = Quiz()
App(my_quiz)
mainloop()



