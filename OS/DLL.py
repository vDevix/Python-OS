import os
import sys
import subprocess

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

def con():
    print()
    print("[ Enter to Continue ]")
    input()
    cl()
    
def home():
    cl()
    subprocess.run(["python", "OS/OS.py"])

def filemanager():
    cl()
    subprocess.run(["python", "OS/File_Manager.py"])
    
def settings():
    cl()
    subprocess.run(["python", "OS/settings.py"])
    
def system():
    cl()
    subprocess.run(["python", "OS/system.py"])
