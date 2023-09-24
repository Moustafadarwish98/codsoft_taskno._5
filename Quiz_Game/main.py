"""Importing classes from files, importing html library to reconfigure acquired
questions to be humanly readable and finally importing the shuffle function from the random
module to shuffle the choices."""
from quiz_data import data
from quiz_model import Questions
from quiz_control import QuizBrain
from ui import QuizInterface
import html
from random import shuffle

question_bank = []

"""Loop to create a question model for all loaded questions."""
for i in range(0, len(data)):
    choices = []

    """Using the unescape method from the html module to make the returned data
    humanly understandable."""
    correct_answer = html.unescape(data[i]["correct_answer"])
    questions = html.unescape(data[i]["question"])
    incorrect_answers = data[i]["incorrect_answers"]

    """Adding the incorrect answers and the correct answer to choices list."""
    for item in incorrect_answers:
        choices.append(html.unescape(item))
    choices.append(correct_answer)

    """Shuffle to randomise correct answer position. """
    shuffle(choices)

    """Creating a new model object for each question"""
    new_model = Questions(questions, choices, correct_answer)
    question_bank.append(new_model)

"""Creating an object of the quiz brain and the interface."""
quiz = QuizBrain(question_bank)
interface = QuizInterface(quiz)







