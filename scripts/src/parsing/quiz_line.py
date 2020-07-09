from linetypes import LineType


class QuizLine:
    """ QuizLine class """

    def __init__(self, line_type: LineType, text: str, is_latex: bool = False):
        """ Create a line of a quiz with a type, text and whether it is Latex or not """
        self.line_type = line_type
        self.text = text
        self.is_latex = is_latex
