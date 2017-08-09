#! python3
import os
"""
Project File Creator
Coded by: Christopher Geiger
Purpose: Manage projects, test, and homework received in college
"""

directory = r"C:\Users\chris\Desktop\College"
os.chdir(directory)


def clear():
    input("Hit enter to continue...")
    print('\n'*30)


def print_cwd():
    print("Current dir: ", str(os.getcwd()))


def yes_input():
    """Get a True or False response from the user"""
    while True:
        usr_input = input("Enter yes or no: ").strip().lower()
        if usr_input == 'y' or usr_input == 'ye' or usr_input == 'yes':
            return True
        elif usr_input == 'n' or usr_input == 'no':
            return False
        print("Please try again.\n")


def print_folders():
    """Print the files/folders in the cwd"""
    print_cwd()
    files = os.listdir(os.getcwd())  # List of all of the files/folders in the cwd
    print("Files/Folders in the current dir: ")
    for file in files:
        print('\t' + file)


def get_files():
    """Get a list of files/folders in the cwd"""
    return os.listdir(os.getcwd())


# Prompt the user with a greeting
print("Hello!\nThis program was created to help you manage your projects and homework!")
clear()

# Start cwd from the College folder
print_cwd()
print("Change the starting directory?")
if yes_input():
    directory = input("Enter a new directory: ")
    os.chdir(directory)
    print_cwd()
else:
    print("The starting directory will remain: " + os.getcwd())

# Navigate the user to their class folder
# Allow the user to select a class folder as a directory
while True:
    clear()
    print_folders()
    files = get_files()
    print("\nNavigate to a class folder: ")
    usr_input = input().lower().strip()
    if not files:
        break

    selection_found = False  # Tell if the user's directory choice was found
    for file in files:
        if usr_input in file.strip().lower():  # Check if the user chose this file
            new_dir = os.path.join(os.getcwd(), file)
            print("Change the cwd to", str(new_dir), "?")
            if yes_input():
                selection_found = True
                directory = new_dir
                clear()
                os.chdir(directory)
                print_cwd()
                break
            else:
                continue

    if not selection_found:  # If no file match was found
        print("Your selection wasn't found...")
        continue

    print("Navigate further? ")
    if yes_input():
        pass
    else:
        break
clear()
print_cwd()

# Ask the user to name the project
project_name = input("Enter a name for your new project: ").strip()

# Create a project folder within the class folder
os.mkdir(os.path.join(os.getcwd(), project_name))

# Navigate to that folder
os.chdir(os.path.join(os.getcwd(), project_name))

# Create a To Do txt file in the selected project
print("Creating a ToDo.txt file...")
toDo = open('ToDo.txt', 'w')
toDo.close()

# Create a Brainstorm txt file in the selected project
print("Creating a Brainstorm.txt file...")
bs = open("BrainStorm.txt", 'w')
bs.close()

# Create a before you hand in text file in the selected project
print("Creating a BEFORE_YOU_HAND_IN.txt file...")
byhi = open("BEFORE_YOU_HAND_IN.txt", 'w')
byhi.close()

# Ask the user to create a docx file / what to name it / how many
print("Create a docx file?")
while True:
    if yes_input():
        docx_name = input("What should I name it? ")
        # Create docx file
        doc = open(docx_name + '.docx', 'w')  # What's up, docx?
    else:
        break
    print("Create another?")

# Ask the user to create an excel file / what to name it / how many
print("Create an excel file?")
while True:
    if yes_input():
        docx_name = input("What should I name it? ")
        # Create xlsx file
        doc = open(docx_name + '.xlsx', 'w')
    else:
        break
    print("Create another?")

print('\nEnd of program')
clear()
# End of program

