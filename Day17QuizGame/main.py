from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = [Question(x["text"], x["answer"]) for x in question_data]

myQuizBrain = QuizBrain(question_bank)

while myQuizBrain.still_has_questions():
    myQuizBrain.next_question()
print(f"Your final score is {myQuizBrain.score}/{len(myQuizBrain.question_list)}.")