from conversion.quiz_to_js.src.parse_quiz import parse_file_to_quiz
from conversion.quiz_to_js.src.quiz.quiz import Quiz
from conversion.quiz_to_js.src.utils.json_encoder import ComplexEncoder
from typing import List
import json


def generate_js_file_for_quiz(quiz_const: str, quiz: Quiz):
    """ Generate a Javascript file for a Quiz """
    js_file = open("%s.quiz.js" % quiz_const, "w+")

    js_file.write("export const %s = %s;" %
                  (quiz_const, json.dumps(quiz, cls=ComplexEncoder, indent=2)))

    js_file.close()


# TODO: find a suitable name
def generate_js_file_for_list_of_quizzes(quizzes: List[str]):
    """ Generate a Javascript file which contains a list of quizzes (const variables) """
    js_file = open("quizzes.js", "w+")

    for q in quizzes:
        js_file.write("import {%s} from './%s.quiz.js';\n" % (q, q))

    js_file.write("\n")
    js_file.write("export const QUIZZES = [%s];" % ', '.join(quizzes))

    js_file.close()
