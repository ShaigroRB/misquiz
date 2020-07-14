import unittest
from conversion.quiz_to_js.src.parse_quiz import parse_line_to_quiz_line
from conversion.quiz_to_js.src.parsing.line_types import LineType
from conversion.quiz_to_js.src.parsing.quiz_line import QuizLine


class TestParseLineToQuizLine(unittest.TestCase):
    """ Test class for testing parsing line to quiz line """

    def test_name_of_quiz_line_type(self):
        text = "N: I am a test quiz."

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.NAME_OF_QUIZ, quiz_line.line_type)

    def test_name_of_quiz_text(self):
        text = "N: I am a test quiz."

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("I am a test quiz.", quiz_line.text)

    def test_question_line_type(self):
        text = "Q: What is this file for?"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.QUESTION, quiz_line.line_type)

    def test_question_text(self):
        text = "Q: What is this file for?"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("What is this file for?", quiz_line.text)

    def test_correct_answer_line_type(self):
        text = "T: A test"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.CORRECT_ANSWER, quiz_line.line_type)

    def test_correct_answer_text(self):
        text = "T: A test"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("A test", quiz_line.text)

    def test_incorrect_answer_line_type(self):
        text = "F: A book"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.INCORRECT_ANSWER, quiz_line.line_type)

    def test_incorrect_answer_text(self):
        text = "F: A book"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("A book", quiz_line.text)

    def test_help_line_type(self):
        text = "H: There is no help for you."

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.HELP, quiz_line.line_type)

    def test_help_text(self):
        text = "H: There is no help for you."

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("There is no help for you.", quiz_line.text)

    def test_empty_newline_line_type(self):
        text = "\n"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.EMPTY, quiz_line.line_type)

    def test_empty_newline_text(self):
        text = "\n"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual("", quiz_line.text)

    def test_incorrect_format_line_type(self):
        text = "S: hello there"

        quiz_line = parse_line_to_quiz_line(text)

        self.assertEqual(LineType.INCORRECT_FORMAT, quiz_line.line_type)
