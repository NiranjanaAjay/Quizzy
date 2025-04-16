from tkinter import *
from typing import get_overloads

from quiz_brain import QuizBrain

THEME_COLOR = "indianRed3"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzy!")
        self.window.config(padx = 20,pady = 20, bg = THEME_COLOR)
        self.window.geometry('350x500')

        self.score = Label(text = "Score : 0", bg = THEME_COLOR, font=("Ariel",10,"bold"),fg="white")
        self.score.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height =250)
        self.canvas.grid(row=1,column =0,columnspan = 2, pady =10)
        self.question = self.canvas.create_text(150,125,text="hello", width=280, font=("Ariel",15,"italic"), fill="black")

        correct = PhotoImage(file= "./images/true.png")
        self.correct_button = Button(image=correct, highlightthickness = 0, bg=THEME_COLOR,command=self.correct_button)
        self.correct_button.grid(row = 2, column =0, pady =30)

        wrong = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness = 0, bg=THEME_COLOR,command=self.wrong_button)
        self.wrong_button.grid(row=2, column=1, pady =30)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            ques = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text = ques)
        else:
            self.canvas.itemconfig(self.question,text = f"You have reached the end of the quiz!!\n          Final score : {self.quiz.score}")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_button(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.window.after(1000, self.next_question)

    def wrong_button(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.window.after(1000,self.next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score.config(text= f"Score : {self.quiz.score}")

