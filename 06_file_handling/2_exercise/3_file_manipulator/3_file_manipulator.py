import os

while True:
    user_input = input()
    if user_input == "End":
        break
    command = user_input.split("-")
    action, file_name = command[0], command[1]
    if action == "Create":
        the_file = open(file_name, mode="w")
        the_file.close()

    elif action == "Add":
        with open(file_name, mode="a") as the_file:
            the_file.write(command[2] + "\n")

    elif action == "Replace":
        try:
            with open(file_name, mode="r") as the_file:
                old_str, new_str = command[2], command[3]
                old_contents = the_file.read()
                if old_str in old_contents:
                    new_contents = old_contents.replace(old_str, new_str)
                else:
                    new_contents = old_contents
            with open(file_name, mode="w") as the_file:
                the_file.write(new_contents)
        except(FileNotFoundError):
            print("An error occurred")
            continue

    elif action == "Delete":
        try:
            os.remove(file_name)
        except(FileNotFoundError):
            print("An error occurred")