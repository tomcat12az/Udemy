def get_tasks(filepath="todos/tasks.txt"):
    """ Read a text file and return the list of
    task items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_tasks))


def write_tasks(tasks_arg, filepath="todos/tasks.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        # todo = input("Enter a todo: ") + "\n"
        # file = open('todos.txt', 'r')
        #  Old way to open file before "with" command usage...see below
        # todos = file.readlines()
        # file.close()

        todos = get_tasks()

        # write todo into a file

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        todos.append(todo + '\n')
#  Put in the below argument information just to know how it's linked.
#  This is the same command as the ones below without the arguments.

        write_tasks(todos)

    elif user_action.startswith("show"):
        # Improved command below with command
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_tasks()

        # new_todos = [item.strip('\n') for item in todos] ex..List Comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_tasks()

            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            write_tasks(todos)


        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        # The try command is for "error handling".  This will give tell the
        # user they put in incorrect formatted information.
        try:
            number = int(user_action[9:])

            todos = get_tasks()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_tasks(todos)


            message = f"Task {task_to_remove} was removed from the list!"
            print(message)
        # The except command is used to identify the certain error and what actions to take.
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Bye!")
    
    
    


