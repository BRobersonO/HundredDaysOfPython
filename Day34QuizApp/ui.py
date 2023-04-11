from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH = 300
HEIGHT = 250

class QuizUI:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Time!")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        #canvas
        self.canvas = Canvas(width=WIDTH, height=HEIGHT, background="white")
        self.q_text = self.canvas.create_text(
            WIDTH/2,
            HEIGHT/2,
            width=280,
            text="question placeholder",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.scoreboard = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(row=0, column=1)

        # Buttons
        false_img = PhotoImage(file="Day34QuizApp/images/false.png")
        self.false_button = Button(image=false_img, command=self.answer_false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        true_img = PhotoImage(file="Day34QuizApp/images/true.png")
        self.true_button = Button(image=true_img, command=self.answer_true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text = next_q)
        else:
            self.canvas.itemconfig(self.q_text, text="You're All Done!")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(background="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

