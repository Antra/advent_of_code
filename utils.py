def get_data(file):
    with open(file, 'r') as f:
        content = f.read()

        return content.split('\n')
