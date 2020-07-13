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

    def print(self, indentation: str = "", orig_indentation: str = ""):
        """ Print content of the question """
        print("%sQuestion: %s" % (indentation, self.name))
        print("%sAnswers:" % (indentation + orig_indentation))
        for answer in self.answers:
            answer.print(indentation * 2)
        if (self.help == ""):
            print("%sNo help for this question" %
                  (indentation + orig_indentation))
        else:
            print("%sHelp of this question: %s" %
                  ((indentation + orig_indentation), self.help))
