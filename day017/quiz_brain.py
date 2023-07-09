class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def play(self):
        while not self.reached_end():
            self.show_question()
            self.answer = self.get_answer()
            self.check_answer()
            self.question_number += 1
            print()
        print(f'You\'ve completed the quiz.\nYour final score is {self.score}/{self.question_number}.')

    def show_question(self):
        question = self.question_list[self.question_number]
        print(f'Q.{self.question_number + 1}: {question.text} (True/False): ', end='')
    
    def get_answer(self):
        while True:
            try:
                answer = input()[0].lower()
                if answer in 'tf':
                    return answer
                else:
                    raise ValueError
            except:
                print('Please enter a valid answer.')
    
    def check_answer(self):
        if self.question_list[self.question_number].answer[0].lower() == self.answer:
            self.score += 1
            print(f'You got it right. Your score is {self.score}')
        else:
            print(f'That\'s wrong.')
        print(f'Your score is {self.score}/{self.question_number + 1}')
            
    def reached_end(self):
        if self.question_number == len(self.question_list):
            return True
        return False
    