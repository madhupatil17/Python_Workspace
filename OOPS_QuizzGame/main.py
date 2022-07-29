from question_model import Question
from quiz_brain import QuizzBrain
from data import question_data

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

print(question_bank)
quizz_brain = QuizzBrain(question_bank)
quizz_brain.next_question()
