#! python3

import datetime, os

direct = r"C:\Users\chris\Desktop\College"

now = datetime.datetime.now()


def clear():
    """Clear out console"""
    print()
    input("Hit enter to continue... ")
    print('\n'*30)


def blank_lines():
    """Break up a prompt and the next input"""
    print('\n'*30)


def init_prompt():
    print("Hello!\nThis program was created to help you organize your college files!")
    print("The year is", str(now.year) + ".")
    blank_lines()
    clear()


def check_dir(directory):
    blank_lines()
    if os.path.exists(directory):
        print("I have discovered a \"College\" folder at", directory)
        print("Should I use this to create your semester directory?")
        usr = input().strip().lower()
        if usr == "y" or usr == "ye" or usr == "yes":
            print("Ok. I'll use the directory at", directory)
        else:
            print("What directory should I use instead?")
            directory1 = input()
            if directory1 == '':
                print("The directory will remain the same.")
            else:
                directory = directory1
    clear()
    return directory


def get_classes():
    """Parse all of the semester's class from the user as a list"""
    blank_lines()
    print("Current dir: " + str(os.getcwd()))
    print()
    print("Please enter all of your classes, line by line, here: ")

    classes = []
    while True:
        c = input()
        if c == '' or c.strip().lower() == 'end':
            print("So your classes are the following: ")
            for _class in classes:
                print(_class)
            print("Is this correct?")
            usr_input = input().strip().lower()
            if usr_input == 'ye' or usr_input == 'y' or usr_input == 'yes':
                return classes
            else:
                print("Ok, let's try this again...")
                clear()
                return get_classes()
        else:
            # Check if c is already in the directory
            if c == os.path.basename(os.getcwd()):  # If entered class is already in your semester list
                print(c, 'is already one of your folders!')
                break
            classes.append(c)
    return classes


def create_subfolder(directory):
    """Make a subfolder in the cwd, returns the name of the subfolder"""
    os.chdir(directory)
    now = datetime.datetime.now()

    print("Create a subfolder in " + directory + " :")

    if 5 >= now.month >= 1 or now.month == 12:
        subfolder = str(now.year) + " - Semester B"
    else:
        subfolder = str(now.year) + " - Semester A"

    print("Call this folder:\n\t" + subfolder, "?")
    usr_input = input().strip().lower()
    if usr_input == 'y' or usr_input == 'ye' or usr_input == 'yes':
        pass
    else:
        blank_lines()
        print("Rename the subfolder: ")
        subfolder = input()

    os.makedirs(os.path.join(directory, subfolder))  # Create the subfolder in the directory
    os.chdir(os.path.join(directory, subfolder))

    return subfolder  # Return the name of the new subfolder


def create_class_folders(directory, classes):
    """Create each individual folder for each entered class (within subfolder)"""
    for _class in classes:
        os.makedirs(os.path.join(directory, _class))



init_prompt()
direct = check_dir(direct)

# Prompt the user to create subfolders for the main dir
subfolder_name = create_subfolder(direct)
subfolder_dir = os.path.join(direct, subfolder_name)  # Get the directory of the subfolder

classes = get_classes()
create_class_folders(subfolder_dir, classes)
#err, wrong dir, outside of subfolder