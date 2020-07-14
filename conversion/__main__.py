from conversion.quiz_to_js.src.parse_quiz import parse_file_to_quiz
from conversion.quiz_to_js.src.generate_js import generate_js_file_for_quiz, generate_js_file_for_list_of_quizzes
from conversion.quiz_to_js.src.utils.file import get_compatible_filename, compare_extension
import sys
import os


def parse_quiz_and_generate_js(filename: str, compatible_filename: str):
    ret_value, quiz = parse_file_to_quiz(filename)
    if (ret_value == 0):
        generate_js_file_for_quiz(compatible_filename, quiz)
    return ret_value


def main(argv):
    if (len(argv) != 1):
        print("❓ - Help: python -m conversion <folder_to_convert>")
        sys.exit(1)

    quizzes_folder = argv[0]
    if (not os.path.isdir(quizzes_folder)):
        print("%s/ does not exist!" % quizzes_folder)
        sys.exit(1)

    # TODO: mkdir folder
    threads = []
    quizzes_names = []

    # TODO: benchmark with threads
    # parse quizzes and generate js for each of them
    for filename in os.listdir(quizzes_folder):
        if (not compare_extension(filename, '.quiz')
                and not compare_extension(filename, '.QUIZ')):
            print('⚠️ - Given file is not of .QUIZ extension: ', filename)
            continue

        compatible_filename = get_compatible_filename(filename, ".quiz")
        fullpath_filename = quizzes_folder.rstrip('/') + '/' + filename
        ret_value = parse_quiz_and_generate_js(fullpath_filename, compatible_filename)
        if (ret_value == 0):
            quizzes_names.append(compatible_filename)

    # create file regrouping all quizzes
    generate_js_file_for_list_of_quizzes(quizzes_names)


if __name__ == '__main__':
    main(sys.argv[1:])
