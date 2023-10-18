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

        with open('todos/tasks.txt', 'r') as file:
            todos = file.readlines()

        # write todo into a file

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        todos.append(todo + '\n')

        with open('todos/tasks.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        # Improved command below with command
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('todos/tasks.txt', 'r') as file:
            todos = file.readlines()

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

            with open('todos/tasks.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            with open('todos/tasks.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        # The try command is for "error handling".  This will give tell the
        # user they put in incorrect formatted information.
        try:
            number = int(user_action[9:])

            with open('todos/tasks.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos/tasks.txt', 'w') as file:
                file.writelines(todos)

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
    
    
    


