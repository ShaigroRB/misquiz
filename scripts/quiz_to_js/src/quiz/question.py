from .answer import Answer


class Question:
    """ Question class """

    def __init__(self, question: str):
        """ Create a question given a question's title """
        self.name = question
        self.answers = []
        self.help = ""

    def add_answer(self, answer: Answer):
        """ Add an answer to the question """
        self.answers.append(answer)

    def add_help(self, help: str):
        """ Add help to the question """
        self.help = help
