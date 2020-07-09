class Answer:
    """ Answer class """

    def __init__(self, is_correct: bool, answer: str):
        """ Create an answer marked as correct or incorrect given a name and a boolean """
        self.is_correct = is_correct
        self.answer = answer
