import os.path
import time
import sys
file = open("default", "r+")


def file_select():
    prompt1 = ""
    global file

    while prompt1.lower() not in ["new", "select"]:
        prompt1 = input("What would you like to do(File)\nNew\nSelect\n>>>")
    if prompt1.lower() == "new":
        name_prompt = "!"
        while name_prompt.strip(" ") == "!":
            name_prompt = input(
                "Name the new file \n(you cant change this later) \n!!!make sure your file name \nis different from "
                "others!!! \n>>>")

        file = open(name_prompt, "w+")
        file.close()
        print(f"New file {name_prompt} created ")
        time.sleep(1)
        os.system("clear")
        file_select()
    elif prompt1.lower() == "select":
        while True:
            selection = input("Whats the Name\nof the file\n>>>")
            finder = file_checker(selection)
            if finder:
                open_ = input("File found\nview>\nedit>\ndelete>\n>>>")
                while open_.lower() not in ["edit", "view", "delete"]:
                    open_ = input(">>>")
                if open_.lower() == "edit":
                    file = open(selection, "a")
                    file.close()
                    print("file successfully opened")
                    file_editor(selection)
                elif open_.lower() == "delete":
                    os.remove(selection)
                    print("file deleted")
                elif open_.lower() == "view":
                    view_file(selection)
            elif not finder:
                no_file_prompt = ""
                while no_file_prompt.lower() not in ["new", "quit"]:
                    no_file_prompt = (
                        f"No file \"{selection}\" found\n would you like to make a new file?\nNew>\nQuit>\n>>>")
                if no_file_prompt.lower() == "new":
                    file = open(selection, "w+")
                    file.close()
                    print("file created")
                    os.system("clear")
                    file_select()
                elif no_file_prompt.lower() == "quit":
                    print("Returning to menu")
                    for character in "...":
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.5)
                    os.system("clear")
                    file_select()


def file_checker(file_name):
    if os.path.exists(file_name):
        return True
    else:
        return False


def file_editor(selection):
    global file
    mode = ""
    print(f"anything you type will be added to \"{selection}\" \nline by line \ntype DONE to return to selection")
    while mode != "DONE":
        change = input(">>>")
        if change == "DONE":
            mode = "DONE"
        else:
            write_file(selection, change)
    file.close()
    file_select()


def write_file(selection, line):
    os.system("clear")
    file2 = open(selection, "a")
    file2.write(f"{line}\n")
    file2.close()


def view_file(selection):
    os.system("clear")
    text = ""
    file3 = open(selection, "r")
    for line in file3:
        for character in line:
            text += character
    print(text)
    file3.close()
    file_select()


file_select()
