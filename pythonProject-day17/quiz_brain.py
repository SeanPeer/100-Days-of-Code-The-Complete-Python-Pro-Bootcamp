
class Quiz:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
       while self.is_there_question():
            current = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q# {self.question_number}: {current.text} - (True/False)")
            self.check_answer(user_answer, current.answer)

    def is_there_question(self):
        return self.question_number < 10

    def check_answer(self,user_answer, true_answer):
        if user_answer == true_answer:
            print("correct! ")
            self.score += 1