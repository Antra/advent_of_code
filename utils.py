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
