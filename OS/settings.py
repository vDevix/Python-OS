import os
import sys
import DLL
import subprocess

def change_name():
    try:
        new_name = input("Enter your new name: ")
        with open("OS/user.txt", "w") as f:
            f.write(new_name)
        print("Name updated successfully!")
        DLL.con()
    except Exception as e:
        print("Error Updating Name")
        DLL.con()
        
def change_pin():
    try:
        new_name = input("Enter your new Pin: ")
        with open("OS/pin.txt", "w") as f:
            f.write(new_name)
        print("Successfully updated Pin")
        DLL.con()
    except Exception as e:
        print("Error Updating Pin")
        DLL.con()
        
while True:
        DLL.cl()
        print("</-- Settings --\>")
        print()
        print("[1] - Change Name")
        print("[2] - Change Pin")
        print("[3] - ?")
        print("[4] - ?")
        print("[5] - ?")
        print("[0] - Exit")
        print("")
        usr = input("Enter Option: ")
        DLL.cl()

        if usr == "1":
            change_name()
        elif usr == "2":
            change_pin()
        elif usr == "3":
            print("Does not exist yet.")
            DLL.con()
        elif usr == "4":
            print("Does not exist yet.")
            DLL.con()
        elif usr == "5":
            delete_file()
        elif usr == "0":
            print("Goodbye.")
            DLL.con()
            DLL.home()
            sys.exit()
        else:
            print("Invalid option.")
            DLL.con()
