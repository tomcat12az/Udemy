# from functions import get_tasks, write_tasks
import functions

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

        todos = functions.get_tasks()

        # write todo into a file

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        todos.append(todo + '\n')
#  Put in the below argument information just to know how it's linked.
#  This is the same command as the ones below without the arguments.

        functions.write_tasks(todos)

    elif user_action.startswith("show"):
        # Improved command below with command
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_tasks()

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

            todos = functions.get_tasks()

            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            functions.write_tasks(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        # The try command is for "error handling".  This will give tell the
        # user they put in incorrect formatted information.
        try:
            number = int(user_action[9:])

            todos = functions.get_tasks()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_tasks(todos)
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
    
    
    


