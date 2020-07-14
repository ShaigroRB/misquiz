from .question import Question


class Quiz:
    """ Quiz class """

    def __init__(self, name: str):
        """ Create a quiz given a name """
        self.name = name
        self.questions = []

    def add_question(self, question: Question):
        """ Add a question to the quiz' questions """
        self.questions.append(question)

    def print(self, indentation: str = " "):
        """ Print the content of the quiz """
        print("Quiz:", self.name)
        print("%sQuestions:" % indentation)
        for question in self.questions:
            print()
            question.print(indentation * 2, indentation)

    def to_json(self):
        """ Return the quiz in JSON format """
        return dict(quiz=self.name, questions=self.questions)
