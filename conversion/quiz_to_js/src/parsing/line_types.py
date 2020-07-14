from enum import Enum, auto


class LineType(Enum):
    """ Type of line (quiz name, question, correct answer, incorrect answer and help) """
    NAME_OF_QUIZ = auto()
    QUESTION = auto()
    CORRECT_ANSWER = auto()
    INCORRECT_ANSWER = auto()
    HELP = auto()
    EMPTY = auto()
    INCORRECT_FORMAT = auto()