from .utils.file import open_file_for_read, close_file, compare_extension
from .parsing.quiz_line import QuizLine
from .parsing.line_types import LineType
import sys


def parse_line_to_quiz_line(line: str):
    """ Parse a line to a QuizLine object """
    line_type = LineType.EMPTY
    line_type_as_str = ""
    text = ""

    data = line.split(" ", 1)
    line_type_as_str = data[0]

    if (len(data) == 2):
        text = data[1]

    if ("N:" == line_type_as_str):
        line_type = LineType.NAME_OF_QUIZ
    elif ("Q:" == line_type_as_str):
        line_type = LineType.QUESTION
    elif ("T:" == line_type_as_str):
        line_type = LineType.CORRECT_ANSWER
    elif ("F:" == line_type_as_str):
        line_type = LineType.INCORRECT_ANSWER
    elif ("H:" == line_type_as_str):
        line_type = LineType.HELP
    elif ("\n" != line_type_as_str):
        line_type = LineType.INCORRECT_FORMAT

    return QuizLine(line_type, text)


def parse_file_as_quiz(filename: str):
    """ Parse a quiz file (.quiz extension) and returns a Quiz object """
    if (not compare_extension(filename, '.quiz')
            and not compare_extension(filename, '.QUIZ')):
        print('Given file is not of .QUIZ extension: ', filename)
        sys.exit(2)
    quiz_file = open_file_for_read(filename)
    close_file(quizFile)
