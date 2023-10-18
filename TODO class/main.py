while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action :
        case 'add':
            todo = input("Enter a todo: ") + "\n"
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

            todos.append(todo)

            with open('todos/tasks.txt', 'w') as file:
                file.writelines(todos)

        case 'show' :
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
        case 'edit' :
            number = int(input("Number of the todo to edit. "))
            number = number - 1

            with open('todos/tasks.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            with open('todos/tasks.txt', 'w') as file:
                file.writelines(todos)

        case 'complete' :
            number = int(input("Number of the task to edit: "))
            todos.pop(number - 1)

            with open('todos/tasks.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            with open('todos/tasks.txt', 'w') as file:
                file.writelines(todos)

            message = f"Task {task_to_remove} was removed from the list!"
            print(message)

        case 'exit':
            break
        

print("Bye!")
    
    
    


