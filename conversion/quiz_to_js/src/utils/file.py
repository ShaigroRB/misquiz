import typing


def open_file_for_read(filename: str):
    """ Open file for read only """
    return open(filename, 'r')


def close_file(file: typing.TextIO):
    """ Close file """
    file.close()


def compare_extension(filename: str, expected_extension: str):
    """ Compare the extension of the given file with the expected extension """
    return filename.endswith(expected_extension)
