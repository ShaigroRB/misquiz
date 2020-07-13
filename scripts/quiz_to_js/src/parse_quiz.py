from utils.file import open_file_for_read, close_file, compare_extension
from parsing.quiz_line import QuizLine
from parsing.line_types import LineType
from quiz.quiz import Quiz
from quiz.question import Question
from quiz.answer import Answer
import sys
# TODO: change back to relative path later


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


def parse_file_to_quiz(filename: str):
    """ Parse a quiz file (.quiz extension) and returns a Quiz object """
    ret_value = 0
    if (not compare_extension(filename, '.quiz')
            and not compare_extension(filename, '.QUIZ')):
        print('Given file is not of .QUIZ extension: ', filename)
        ret_value = 2
        return (ret_value, None)

    quiz_file = open_file_for_read(filename)
    current_line = quiz_file.readline()

    quiz: Quiz = None
    current_question: Question = None
    is_quiz_correct = True
    index = 0

    while (current_line != ""):
        current_quiz_line = parse_line_to_quiz_line(current_line)
        index += 1

        if (current_quiz_line.line_type == LineType.INCORRECT_FORMAT):
            print('Wrong format of line %d > %s' % (index, current_line))
            is_quiz_correct = False
            ret_value = 2
        elif (is_quiz_correct):
            if (current_quiz_line.line_type == LineType.NAME_OF_QUIZ):
                quiz = Quiz(current_quiz_line.text)
            elif (current_quiz_line.line_type == LineType.QUESTION):
                current_question = Question(current_quiz_line.text)
                quiz.add_question(current_question)
            elif (current_quiz_line.line_type == LineType.CORRECT_ANSWER):
                answer = Answer(True, current_quiz_line.text)
                current_question.add_answer(answer)
            elif (current_quiz_line.line_type == LineType.INCORRECT_ANSWER):
                answer = Answer(False, current_quiz_line.text)
                current_question.add_answer(answer)
            elif (current_quiz_line.line_type == LineType.HELP):
                question_help = current_quiz_line.text
                current_question.add_help(question_help)

        current_line = quiz_file.readline()

    close_file(quiz_file)

    return (ret_value, quiz)
