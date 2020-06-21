from question import Question


class Quiz:
    """ Quiz class """

    def __init__(self, name: str):
        """ Create a quiz given a name """
        self.name = name
        self.questions = []

    def add_question(self, question: Question):
        """ Add a question to the quiz' questions """
        self.questions.append(question)
