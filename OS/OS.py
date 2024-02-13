# -- Library -- #
import os
import sys
import subprocess
import DLL


# -- Funcations -- #
def stored_user():
    try:
        with open("OS/user.txt", "r") as file:
            user = file.read()
        return user
    except FileNotFoundError:
        print("User file not found.")
        return None

# -- Variables -- #
user = stored_user()

# -- Menu -- #
def main_menu():
    while True:
        DLL.cl()
        print("""
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░░╚════╝░╚═════╝░
by Devix
""")
        
        print(f"Welcome, {user}")
        print()
        print("[1] - ?")
        print("[2] - ?")
        print("[3] - ?")
        print("[4] - File Manager")
        print("[5] - Settings")
        print("[0] - Shutdown")
        print()
        usr = input("Enter Option: ")
        DLL.cl()

        if usr == "1":
            print("Does not exist yet.")
            DLL.con()
        elif usr == "2":
            print("Does not exist yet.")
            DLL.con()
        elif usr == "3":
            print("Does not exist yet.")
            DLL.con()
        elif usr == "4":
            DLL.filemanager()
        elif usr == "5":
            DLL.settings()
        elif usr == "0":
            print("Shutting Down...")
            DLL.con()
            sys.exit()
        else:
            print("Invalid option.")
            DLL.con()

if __name__ == "__main__":
    main_menu()
