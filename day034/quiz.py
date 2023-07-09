import requests
import html


class Quiz:
    # TDB_URL = 'https://opentdb.com/api.php?amount=10&type=boolean'
    TDB_URL = 'https://opentdb.com/api.php'
    PARAMS = {
        'amount': 10,
        'type': 'boolean'
    }
    HTML_ENTITIES = {}

    def __init__(self) -> None:
        try:
            self.questions = self.get_questions()
        except Exception as e:
            print('Error occurred when fetching questions.')
            print(e)
            raise NotImplementedError
        else:
            self.score = 0
            self.next_question()

    def get_questions(self) -> list:
        response = requests.get(Quiz.TDB_URL, Quiz.PARAMS)
        response.raise_for_status()
        return response.json()['results']
    
    def next_question(self) -> None:
        try:
            self.question = self.questions.pop()
            # unescape html entities in the question
            self.question['question'] = html.unescape(self.question['question'])
            # print(self.question)
        except:
            self.question = None
        
    def check_answer(self, answer: str) -> bool | None:
        if self.question:
            if self.question['correct_answer'] == answer:
                self.score += 1
                return True
            else:
                return False
        return None
        

