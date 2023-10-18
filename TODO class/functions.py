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
# The below command will only be run inside this program.
# When you call this program it will not show the commands below.


if __name__ == "__main__":
    print("Hello")
    print(get_tasks())