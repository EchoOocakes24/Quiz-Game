THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", anchor="s", background=THEME_COLOR, fg="white",
                                 font=("Arial", 11, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                 font=("Arial", 18, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.true_image, highlightthickness=0, command=self.true_answer)
        self.check_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.false_image, highlightthickness=0, command=self.false_answer)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.questions, text=question_text)

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
