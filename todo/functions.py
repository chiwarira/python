def get_todos(filepath='todo/todos.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_args, filepath='todo/todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)