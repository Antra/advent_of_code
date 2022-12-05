def get_data(file):
    with open(file, 'r') as f:
        content = f.read()

        return content.split('\n')


def read_text_file_lines(file):
    """reads a text file and returns the content split line by line

    Args:
        file (str): filename of the file to read; either in the same folder or including the path
    """
    with open(file, 'r') as f:
        content = f.read()

        return content.split('\n')


def splitter(sequence, sep=''):
    """split sequence into sub-sequences on a separator

    Args:
        sequence (list): the sequence to split apart
        sep (str, optional): the separator sequence. Defaults to ''.

    Yields:
        subsequence (list of int): yields a subsequence as int from the original sequence
    """
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk
