import unittest
from unittest.mock import Mock
from conversion.quiz_to_js.src.quiz.quiz import Quiz
from conversion.quiz_to_js.src.quiz.question import Question
from conversion.quiz_to_js.src.quiz.answer import Answer


class TestToJson(unittest.TestCase):
    """ Test class for testing to_json method of classes of the quiz module """

    def test_to_json_quiz_no_question(self):
        quiz = Quiz("This is a quiz")

        encoding = quiz.to_json()

        self.assertDictEqual(
            dict(quiz="This is a quiz", questions=[]), encoding)

    def test_to_json_quiz_one_question(self):
        quiz = Quiz("My quiz")
        question = Mock()
        quiz.add_question(question)

        encoding = quiz.to_json()

        self.assertDictEqual(
            dict(quiz="My quiz", questions=[question]), encoding)

    def test_to_json_quiz_multiple_question(self):
        quiz = Quiz("My quiz")
        q1 = Mock()
        q2 = Mock()
        q3 = Mock()
        quiz.add_question(q2)
        quiz.add_question(q1)
        quiz.add_question(q3)

        encoding = quiz.to_json()

        self.assertDictEqual(
            dict(quiz="My quiz", questions=[q2, q1, q3]), encoding)

    def test_to_json_question_no_answer_no_help(self):
        question = Question("My test question")

        encoding = question.to_json()

        self.assertDictEqual(
            dict(question="My test question", answers=[], help=""), encoding)

    def test_to_json_question_no_answer_and_help(self):
        question = Question("My test question")
        question.add_help("My help")

        encoding = question.to_json()

        self.assertDictEqual(
            dict(question="My test question", answers=[], help="My help"), encoding)

    def test_to_json_question_answer_no_help(self):
        question = Question("Cookie question")
        answer = Mock()
        question.add_answer(answer)

        encoding = question.to_json()

        self.assertDictEqual(
            dict(question="Cookie question", answers=[answer], help=""), encoding)

    def test_to_json_question_answer_help(self):
        question = Question("Cookie question")
        answer = Mock()
        question.add_answer(answer)
        question.add_help("Unicorn incoming!")

        encoding = question.to_json()

        self.assertDictEqual(dict(question="Cookie question", answers=[
                             answer], help="Unicorn incoming!"), encoding)

    def test_to_json_correct_answer(self):
        answer = Answer(True, "This is true")

        encoding = answer.to_json()

        self.assertDictEqual(
            dict(isCorrect=True, answer="This is true"), encoding)

    def test_to_json_incorrect_answer(self):
        answer = Answer(False, "This is not good")

        encoding = answer.to_json()

        self.assertDictEqual(
            dict(isCorrect=False, answer="This is not good"), encoding)
