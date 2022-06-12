from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for each_item in question_data:
    question_bank.append(Question(each_item["question"], each_item["correct_answer"]))


que = QuizBrain(question_bank)

while que.still_has_question():
    que.next_question()

print("you have completed the quiz")
print(f"The final score is {que.score}/{que.question_number}")
