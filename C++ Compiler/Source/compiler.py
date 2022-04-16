# Created by Wallee#8314/Red-exe-Engineer for compiling C++ programs with g++

# Imoprt stuff from Tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Import run and find_executable
from subprocess import run
from distutils.spawn import find_executable

# Import argv for useless system arguments
from sys import argv

# Set command = g++
command = "g++"

# check if the len ar argv is 2
if len(argv) == 2:

    # Check if the second index of argv is -gcc
    if argv[1] == "-gcc":

        # Use find_executable to see if the user doesn't have gcc installed on their system
        if find_executable("g++") == None:

            # Exit
            exit("Unable to find gcc")

        # The user does have gcc installed on their system to set command to gcc
        command = "gcc"

    # Check if the second index of argv is -help
    elif argv[1] == "-help":

        # Exit with some info
        exit("Created by Wallee#8314/Red-exe-Engineer\n Use -gcc to use the gcc compiler instead of g++\n Though it is kinda broken :p")

    # Else the provided argument has not been found
    else:

        # Exit
        exit("Argument error, see -help for more info")

# Else check if the len of argv is creater than 2
elif len(argv) > 2:

    # Exit because there are no arguments that need another argument
    exit("Too many arguments")

# Check if g++ is installed and the command is g++
if find_executable("g++") == None and command == "g++":

    # Exit
    exit("Unable to find g++ package")


# Make a root window and hide it ASAP
root = Tk()
root.withdraw()

# Ask the user for a file
file = askopenfilename(
    title = "Select a file",
    filetypes = [
        ("C++", "*.cpp"),
        ("C", "*.c"),
        ("All", "*")
    ]
)

# Check if the user didn't pick a file
if file == ():
    exit()

# Set fileName to the last part of file
fileName = file.split("/")[-1]

# Ask for a save path
path = asksaveasfilename(
    title = "Export location",
    initialfile = fileName.split(".")[0]
)

# Check of the path is empty
if path == "":

    # Exit
    exit()

# Ask for some optional arguments
options = simpledialog.askstring(
    title = "Optional arguments",
    prompt = ""
)

# Check if arguments is None, which means the user closed the window
if options == None:

    # Exit
    exit()

# Setup a popup window
popup = Tk()

# Try something that may cause an error
try:

    # Run a process to compile the program
    run(
        args = f'{command} {file} -o {path} {options}',
        shell = True,
        check = True
    )

    # Add some widgets to popup
    popup.wm_title("Complete")
    label = Label(popup, text = f'Successfully compiled {path.split("/")[-1]}')

# Something went wrong
except Exception as error:

    # Add some widgets to popup
    popup.wm_title("Oops!")
    label = Label(popup, text = "Could not compile {}\n".format(fileName) + str(error))

# Pack the label
label.pack(side="top", fill="x", pady=10)

# Add a close widget to popup and pack it
close = Button(popup, text="Close", command = exit)
close.pack()

# Make the popup not resizable
popup.resizable(False, False)

# Start the popup
popup.mainloop()

# Exit the program
exit()
