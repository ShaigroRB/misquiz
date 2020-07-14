import unittest
import json
from quiz_to_js.src.quiz.quiz import Quiz
from quiz_to_js.src.quiz.question import Question
from quiz_to_js.src.quiz.answer import Answer
from quiz_to_js.src.utils.json_encoder import ComplexEncoder


class TestJsonEncoding(unittest.TestCase):
    """ Test class for testing json encoding of classes of quiz module """

    def test_json_encoding_answer(self):
        answer = Answer(False, "Nothing special")

        encoding = json.dumps(answer.to_json())

        self.assertEqual(
            '{"isCorrect": false, "answer": "Nothing special"}',
            encoding
        )

    def test_json_encoding_question_no_answer_help(self):
        question = Question("What is this file for?")
        question.add_help("There is no help for you")

        encoding = json.dumps(question.to_json())

        self.assertEqual(
            '{"question": "What is this file for?", "answers": [], "help": "There is no help for you"}',
            encoding
        )

    def test_json_encoding_question_answer_help_with_ComplexEncoder(self):
        question = Question("What is this file for?")
        answer = Answer(True, "A test")
        question.add_answer(answer)
        question.add_help("There is no help for you")

        encoding = json.dumps(question.to_json(), cls=ComplexEncoder)

        self.assertEqual(
            '{"question": "What is this file for?", "answers": [{"isCorrect": true, "answer": "A test"}], "help": "There is no help for you"}',
            encoding
        )

    def test_json_encoding_question_answer_help_without_ComplexEncoder(self):
        question = Question("What is this file for?")
        answer = Answer(True, "A test")
        question.add_answer(answer)
        question.add_help("There is no help for you")

        self.assertRaises(TypeError, json.dumps, question.to_json())

    def test_json_encoding_question_multiple_answers_help(self):
        question = Question("What is this file for?")
        a1 = Answer(True, "A test")
        a2 = Answer(False, "A book")
        a3 = Answer(False, "Nothing special")
        question.add_answer(a1)
        question.add_answer(a2)
        question.add_answer(a3)
        question.add_help("There is no help for you.")

        encoding = json.dumps(question.to_json(), cls=ComplexEncoder)

        self.assertEqual(
            '{"question": "What is this file for?", "answers": [{"isCorrect": true, "answer": "A test"}, {"isCorrect": false, "answer": "A book"}, {"isCorrect": false, "answer": "Nothing special"}], "help": "There is no help for you."}',
            encoding
        )

    def test_json_encoding_quiz_no_question(self):
        quiz = Quiz("I am a test quiz.")

        encoding = json.dumps(quiz.to_json())

        self.assertEqual(
            '{"quiz": "I am a test quiz.", "questions": []}',
            encoding
        )

    def test_json_encoding_quiz_one_question(self):
        quiz = Quiz("I am a test quiz.")
        question = Question("What is this file for?")
        a1 = Answer(True, "A test")
        a2 = Answer(False, "A book")
        a3 = Answer(False, "Nothing special")
        question.add_answer(a1)
        question.add_answer(a2)
        question.add_answer(a3)
        question.add_help("There is no help for you.")
        quiz.add_question(question)

        encoding = json.dumps(quiz.to_json(), cls=ComplexEncoder)

        self.assertEqual(
            '{"quiz": "I am a test quiz.", "questions": [{"question": "What is this file for?", "answers": [{"isCorrect": true, "answer": "A test"}, {"isCorrect": false, "answer": "A book"}, {"isCorrect": false, "answer": "Nothing special"}], "help": "There is no help for you."}]}',
            encoding
        )

    def test_json_encoding_quiz_multiple_questions(self):
        quiz = Quiz("I am a test quiz.")
        question = Question("What is this file for?")
        a1 = Answer(True, "A test")
        a2 = Answer(False, "A book")
        a3 = Answer(False, "Nothing special")
        question.add_answer(a1)
        question.add_answer(a2)
        question.add_answer(a3)
        question.add_help("There is no help for you.")
        quiz.add_question(question)
        q2 = Question("What is this file not for?")
        a_q2 = Answer(False, "A test")
        a2_q2 = Answer(True, "A book")
        a3_q2 = Answer(True, "Nothing special")
        q2.add_answer(a_q2)
        q2.add_answer(a2_q2)
        q2.add_answer(a3_q2)
        quiz.add_question(q2)

        encoding = json.dumps(quiz.to_json(), cls=ComplexEncoder)

        self.assertEqual(
            '{"quiz": "I am a test quiz.", "questions": [{"question": "What is this file for?", "answers": [{"isCorrect": true, "answer": "A test"}, {"isCorrect": false, "answer": "A book"}, {"isCorrect": false, "answer": "Nothing special"}], "help": "There is no help for you."}, {"question": "What is this file not for?", "answers": [{"isCorrect": false, "answer": "A test"}, {"isCorrect": true, "answer": "A book"}, {"isCorrect": true, "answer": "Nothing special"}], "help": ""}]}',
            encoding
        )
