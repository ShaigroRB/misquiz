def compare_extension(filename: str, expected_extension: str):
    """ Compare the extension of the given file with the expected extension """
    return filename.endswith(expected_extension)


def get_compatible_filename(filename: str, extension: str):
    """ Get the filename as a non-problematic string (replace ' ' by '_', ...). Removes the extension. """
    no_ext = str(filename).lower().rstrip(extension)
    return (no_ext).replace(" ", "_").replace("-", "_").replace(".", "_")
