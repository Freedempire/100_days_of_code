from question_model import Question
from quiz_brain import QuizBrain
import data

question_list = []
for question in data.question_data:
    question_list.append(Question(question['text'], question['answer']))

quiz_brain = QuizBrain(question_list)
quiz_brain.play()