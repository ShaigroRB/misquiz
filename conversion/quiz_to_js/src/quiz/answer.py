class Answer:
    """ Answer class """

    def __init__(self, is_correct: bool, answer: str):
        """ Create an answer marked as correct or incorrect given a name and a boolean """
        self.is_correct = is_correct
        self.answer = answer

    def print(self, indentation: str = ""):
        """ Print the content of this answer """
        print_correct = "Correct answer" if self.is_correct else "Incorrect answer"
        print("%s%s: %s" % (indentation, print_correct, self.answer))

    def to_json(self):
        """ Return the answer in JSON format """
        return dict(isCorrect=self.is_correct, answer=self.answer)
