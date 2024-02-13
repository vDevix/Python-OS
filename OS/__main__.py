# -- Libary -- #
import os
import sys
import subprocess
import time
import DLL


# -- Boot  -- #
DLL.cl()
print("Checking: OS")
time.sleep(2)
DLL.cl()


def check_missing_files(directory):
    expected_files = ["__main__.py", "OS.py", "settings.py", "DLL.py", "File_Manager.py", "user.txt", "pin.txt", "system.py", "Files"]
    missing_files = [file for file in expected_files if file not in os.listdir(directory)]
    if missing_files:
        print("Missing files, Please download the OS again.")
        DLL.con()
    else:
        print("Sucessfully Loaded: OS")
        DLL.con()

if __name__ == "__main__":
    directory_path = os.path.dirname(os.path.realpath(__file__))
    check_missing_files(directory_path)

DLL.system()
