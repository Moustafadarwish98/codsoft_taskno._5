"""Importing the tkinter library to create a GUI"""
from tkinter import *
from tkinter import messagebox
from quiz_control import QuizBrain

COLOR = "#154360"


class QuizInterface:
    """To Design and Create a friendly GUI."""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        """Window setup"""
        self.window = Tk()
        self.window.title("Quiz game.")
        self.window.geometry("800x480")
        self.window.config(bg=COLOR, padx=10, pady=20)

        """Labels setup"""
        self.label = Label(text=f"Score: {self.quiz.score}", bg=COLOR, fg="white",
                           highlightthickness=0, font=("Arial", 20, "italic"))
        self.label.grid(row=0, column=0)

        """Canvas setup"""
        self.canvas = Canvas(width=600, height=200)
        self.text = self.canvas.create_text(300, 80, text="Type here.",
                                            font=("Arial", 20, "italic"),
                                            width=600)
        self.canvas.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.var = []

        """A loop to assign a none variable to a variables list"""
        for i in range(0, 4):
            self.var.append(IntVar())

        """Check buttons setup"""
        self.option_1 = Checkbutton(master=self.window, text="first option", bg=COLOR,
                                    highlightthickness=0, pady=5, activebackground=COLOR
                                    , font=("Arial", 12, "italic"), variable=self.var[0],
                                    command=self.checked)
        self.option_2 = Checkbutton(master=self.window, text="second option", bg=COLOR,
                                    highlightthickness=0, pady=5, font=("Arial", 12, "italic"),
                                    activebackground=COLOR, variable=self.var[1],
                                    command=self.checked)
        self.option_3 = Checkbutton(master=self.window, text="third option", bg=COLOR,
                                    highlightthickness=0, pady=5, activebackground=COLOR,
                                    font=("Arial", 12, "italic"), variable=self.var[2],
                                    command=self.checked)
        self.option_4 = Checkbutton(master=self.window, text="fourth option", bg=COLOR,
                                    highlightthickness=0, pady=5,
                                    activebackground=COLOR, font=("Arial", 12, "italic"),
                                    variable=self.var[3], command=self.checked)
        self.option_1.grid(row=2, column=1, sticky="w")
        self.option_2.grid(row=3, column=1, sticky="w")
        self.option_3.grid(row=4, column=1, sticky="w")
        self.option_4.grid(row=5, column=1, sticky="w")

        """Displaying welcome message and Rules"""
        self.canvas.itemconfig(self.text, text="                Welcome to the quiz game! \n\n"
                                               "The quiz is composed of 10 questions. "
                                               "You have to get at least 5 correct answers to pass.\n"
                                               "Good luck!")

        """Buttons setup"""
        self.next = Button(text="Pass", bg=COLOR, highlightthickness=0, font=("Arial", 14, "italic"),
                           command=self.pass_question)
        self.next.grid(row=6, column=2, sticky="e")

        """Asking the user if they want to start"""
        start = messagebox.askyesno(message="Are you ready to start your quiz?")
        if start:
            self.get_next_question()
        else:
            messagebox.showinfo(message="Whenever you are ready.")
        self.window.mainloop()

    def get_next_question(self):
        """Checking if their still question. if yes display the question and the choices,
        if no gives user a feedback on their performance."""
        self.canvas.config(bg="white")
        self.clear_checkboxes()
        if self.quiz.remain_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            options = self.quiz.current_question.all_choices
            self.canvas.itemconfig(self.text, text=question)
            self.option_1.config(text=f"{options[0]}")
            self.option_2.config(text=f"{options[1]}")
            self.option_3.config(text=f"{options[2]}")
            self.option_4.config(text=f"{options[3]}")
        else:
            self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            if self.quiz.score >= 5:
                self.canvas.itemconfig(self.text, text=f"      Quiz is over!\n\nYour final score is {self.quiz.score}"
                                                       f"/10.\n"
                                                       f"You passed!")
            else:
                self.canvas.itemconfig(self.text, text=f"      Quiz is over!\n\nYour final score is {self.quiz.score}/"
                                                       f"10.\n"
                                                       f"You failed.")
            self.option_1.config(text="first option")
            self.option_2.config(text="second option")
            self.option_3.config(text="third option")
            self.option_4.config(text="fourth option")

    def checked(self):
        """Searches for the checked box and send it to check the answer."""
        for i in self.var:
            if i.get() == 1:
                num = self.var.index(i)
                self.check_answer(num)

    def check_answer(self, num):
        """Send user's answer to quiz_control to check if it is correct or not.
        Then gives feedback depending on user's answer."""
        confirm = messagebox.askyesno(message="Confirm your answer?")
        if confirm:
            options = self.quiz.current_question.all_choices
            user_answer = options[num]
            is_correct = self.quiz.check_if_correct(user_answer)
            self.feedback(is_correct)
        else:
            self.clear_checkboxes()
            messagebox.showinfo(message="Choose an answer.")

    def feedback(self, is_correct):
        """Give user feedback based on their answer."""
        if is_correct:
            self.canvas.config(bg="light green")
        else:
            self.canvas.configure(bg="red")
            self.canvas.itemconfig(self.text, text=f"The correct answer is"
                                                   f" {self.quiz.current_question.correct_answer}.")
        self.window.after(2000, self.get_next_question)

    def clear_checkboxes(self):
        """To clear all check boxes."""
        for i in range(0, 4):
            self.var[i].set(0)

    def pass_question(self):
        """To allow the user to skip questions."""
        pass_sure = messagebox.askyesno(message="Are you sure you want to pass question?")
        if pass_sure:
            self.get_next_question()
