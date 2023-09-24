class QuizBrain:
    """Represents the quiz brain. Check if there are questions remaining,
    check the correctness of answers and update score"""
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
        self.current_question = None

    def remain_questions(self):
        """Check there are questions left."""
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        """Get next question text and answers."""
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_number}: {q_text}"

    def check_if_correct(self, selected):
        """Check correctness of user's answer."""
        self.current_question = self.questions_list[self.question_number - 1]
        if selected == self.current_question.correct_answer:
            self.score += 1
            return True
        else:
            return False



