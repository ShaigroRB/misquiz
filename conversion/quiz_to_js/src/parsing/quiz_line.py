from .line_types import LineType


class QuizLine:
    """ QuizLine class """

    def __init__(self, line_type: LineType, text: str, is_latex: bool = False):
        """ Create a line of a quiz with a type, text and whether it is Latex or not """
        self.line_type = line_type
        # let's see if we keep the escape
        self.text = text.rstrip("\n")
        self.is_latex = is_latex
