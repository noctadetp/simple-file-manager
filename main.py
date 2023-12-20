import os
import shutil
from termcolor import colored

def display_menu():
    print(colored("Python File Manager", "yellow"))
    print("--------------------")
    print("1. List files in directory")
    print("2. Create a new directory")
    print("3. Delete a directory")
    print("4. Rename a file or directory")
    print("5. Copy a file or directory")
    print("6. Move a file or directory")
    print("7. Exit")

def list_files():
    path = input("Enter the directory path: ")
    files = os.listdir(path)
    print(colored("Files in directory:", "green"))
    for file in files:
        print(file)

def create_directory():
    path = input("Enter the directory path: ")
    directory = input("Enter the name of the new directory: ")
    os.mkdir(os.path.join(path, directory))
    print(colored("Directory created successfully!", "green"))

def delete_directory():
    path = input("Enter the directory path: ")
    directory = input("Enter the name of the directory to delete: ")
    shutil.rmtree(os.path.join(path, directory))
    print(colored("Directory deleted successfully!", "green"))

def rename_file_or_directory():
    path = input("Enter the file/directory path: ")
    new_name = input("Enter the new name: ")
    os.rename(path, os.path.join(os.path.dirname(path), new_name))
    print(colored("File/directory renamed successfully!", "green"))

def copy_file_or_directory():
    source = input("Enter the source path: ")
    destination = input("Enter the destination path: ")
    shutil.copy(source, destination)
    print(colored("File/directory copied successfully!", "green"))

def move_file_or_directory():
    source = input("Enter the source path: ")
    destination = input("Enter the destination path: ")
    shutil.move(source, destination)
    print(colored("File/directory moved successfully!", "green"))

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        list_files()
    elif choice == "2":
        create_directory()
    elif choice == "3":
        delete_directory()
    elif choice == "4":
        rename_file_or_directory()
    elif choice == "5":
        copy_file_or_directory()
    elif choice == "6":
        move_file_or_directory()
    elif choice == "7":
        print(colored("Exiting...", "yellow"))
        break
    else:
        print(colored("Invalid choice. Please try again!", "red"))
