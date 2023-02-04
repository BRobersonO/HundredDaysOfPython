class QuizBrain:

    def __init__(self,bank) -> None:
        self.question_number = 0
        self.question_list = bank
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} True or False? ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("Correct! +1 ")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The answer is {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1} \n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)