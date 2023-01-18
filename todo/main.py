from functions import get_todos, write_todos
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)
    
    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:
            todo = user_action[5:]
            todos = get_todos()

            number = int(user_action[5:])
            new_todo = input("Enter new todo: ") + "\n"
            todos[number - 1] = new_todo

            write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            number = number - 1
            removed = todos.pop(number).strip('\n')

            write_todos(todos)

            print(f"Todo {removed} was removed from the list")
        except IndexError:
            print(f"There is no item with number {number + 1} in the list")
            continue

    elif user_action.startswith('exit'):
        break  
    else:
        print("Command is not valid.")