from functions import get_todos, write_todos
import time
prompt = 'Type add, show, edit, complete or exit: '


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input(prompt)
    user_action = user_action.strip().lower()
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        todos.append(todo.capitalize())

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)
    elif user_action.startswith("show"):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = get_todos()
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ").capitalize() + "\n"
            todos.__setitem__(number, new_todo)
            write_todos(todos)
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}.{item}")
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("Index not found.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            write_todos(todos)
            message = f"todo {to_remove} was removed from list"
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown code")
print("Bye!")
