# -- Libary -- #
import os
import sys
import time
import DLL
import subprocess

# -- New User -- #
def get_user_name():
    if os.path.exists("OS/user.txt"):
        with open("OS/user.txt", "r") as f:
            user_name = f.read().strip()
        return user_name
    else:
        return None

def set_user_name(name):
    with open("OS/user.txt", "w") as f:
        f.write(name)

if __name__ == "__main__":
    user_name = get_user_name()

    if user_name:
        print("Welcome back, {}!".format(user_name))
        DLL.con()
    else:
        name = input("Welcome, Please enter your name: ")
        set_user_name(name)
        print("Hello, {}! Your name has been saved.".format(name))
        DLL.con()

# -- New Pin -- #
import os

def get_pin():
    if os.path.exists("OS/pin.txt"):
        with open("OS/pin.txt", "r") as f:
            pin = f.read().strip()
        return pin
    else:
        return None

def set_pin(pin):
    with open("OS/pin.txt", "w") as f:
        f.write(pin)

def create_pin():
    DLL.cl()
    pin = input("Enter your new PIN: ")
    set_pin(pin)
    DLL.cl()
    print("PIN successfully created.")

if __name__ == "__main__":
    user_pin = get_pin()

    if user_pin == "False":
        print("")
    elif user_pin:
        while True:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == user_pin:
                print("Access granted.")
                break
            else:
                DLL.cl()
                print("Invalid PIN. Try again.")
    else:
        while True:
            create_new_pin = input("Do you want to create a new PIN? (yes/no): ")
            if create_new_pin.lower() == "yes":
                create_pin()
                break
            elif create_new_pin.lower() == "no":
                set_pin("False")
                break
            else:
                DLL.cl()
                print("Invalid input. Please enter 'yes' or 'no'.")

DLL.home()

