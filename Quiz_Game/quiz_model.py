class Questions:
    """Specify the question text, correct answer and all choices."""
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.all_choices = answers


