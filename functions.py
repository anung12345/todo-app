FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Raed a text file and return the list of to-do items. """
    with open(filepath, 'r') as document:
        todos_local = document.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
