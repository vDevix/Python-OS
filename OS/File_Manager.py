# -- Libary -- #
import os
import sys
import DLL
import subprocess

# -- Functions -- #
def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

def con():
    print()
    print("[ Enter to Continue ]")
    input()
    cl()

import os

def create_file():
    try:
        filename = input("Enter file name to create: ")
        filepath = os.path.join("OS", "Files", filename)
        if os.path.exists(filepath):
            print(f"File '{filename}' already exists.")
        else:
            with open(filepath, 'w') as file:
                print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")
    con()

def edit_file():
    try:
        filename = input("Enter file name to edit: ")
        filepath = os.path.join("OS", "Files", filename)
        if not os.path.exists(filepath):
            print(f"File '{filename}' does not exist.")
        else:
            with open(filepath, 'a') as file:
                content = input("Enter text to append: ")
                file.write(content + "\n")
                print(f"Content appended to '{filename}' successfully.")
    except Exception as e:
        print(f"Error editing file: {e}")
    con()

def read_file():
    try:
        filename = input("Enter file name to read: ")
        filepath = os.path.join("OS", "Files", filename)
        if not os.path.exists(filepath):
            print(f"File '{filename}' does not exist.")
        else:
            with open(filepath, 'r') as file:
                content = file.read()
                print(f"Content of '{filename}':")
                print(content)
    except Exception as e:
        print(f"Error reading file: {e}")
    con()

def list_files():
    try:
        files = os.listdir(os.path.join("OS", "Files"))
        if files:
            print("All Files:")
            for file in files:
                print(file)
        else:
            print("No files found in 'Files' folder.")
    except Exception as e:
        print(f"Error listing files: {e}")
    con()

def delete_file():
    try:
        filename = input("Enter file name to delete: ")
        filepath = os.path.join("OS", "Files", filename)
        if not os.path.exists(filepath):
            print(f"File '{filename}' does not exist.")
        else:
            os.remove(filepath)
            print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")
    con()
# -- Menu -- #
while True:
    cl()
    print("</-- File Manager --\>")
    print()
    print("[1] - Create File")
    print("[2] - Edit File")
    print("[3] - Read File")
    print("[4] - List Files")
    print("[5] - Delete File")
    print("[0] - Exit")
    print("")
    usr = input("Enter Option: ")
    cl()

    if usr == "1":
        create_file()
    elif usr == "2":
        edit_file()
    elif usr == "3":
        read_file()
    elif usr == "4":
         list_files()
    elif usr == "5":
         delete_file()
    elif usr == "0":
        print("Goodbye.")
        con()
        DLL.home()
        sys.exit()
    else:
        print("Invalid option.")
        con()
