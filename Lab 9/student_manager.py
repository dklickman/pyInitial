# This program manages students and their information 

import student
import pickle

# Globals to be used for menu choices
LOOK_UP = 1
ADD = 2
CHANGE_GPA = 3
CHANGE_GRADE = 4
PRINTALL = 5
QUIT = 6

# Global constants for file name
FILENAME = 'student_data.dat'

def main():
    # Load the existing contact dictionary and assign to my contact
    mycontacts = load_contacts()

    # Initialize a variable for the user choice
    choice = 0

    # loop until user decides to quit
    while choice != QUIT:
        # Get the user's menu choice
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(mycontacts)

        elif choice == ADD:
            add(mycontacts)

        elif choice == CHANGE_GPA:
            change_gpa(mycontacts)

        elif choice == CHANGE_GRADE:
            change_grade(mycontacts)

        elif choice == PRINTALL:
            print_all()

    save_contacts(mycontacts)



##### Functions #####

# This loads the contacts into memory
def load_contacts():
    try:
        # open contacts.dat
        input_file = open(FILENAME, 'rb')

        # unpickle from the dictionary
        contact_dct = pickle.load(input_file)

        # close the phone_inventory.dat file
        input_file.close()
    except IOError:
        # create a dictionary file
        contact_dct = {}

    return contact_dct


# This displays the menu 
def get_menu_choice():
    print()
    print("Menu")
    print("____________________")
    print("(1) Look up and print student infomation.")
    print("(2) Add a new student.")
    print("(3) Change student's GPA.")
    print("(4) Change student's expected grade.")
    print("(5) Print all student information.")
    print("(6) Quit (saves all changes)")

    # Get user choice
    choice = int(input("Enter your choice: "))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid menu item number."))
    return choice


# This looks up an item in a certain dictionary
def look_up(mycontacts):
    # Get the name to look up
    name = input("Enter a name to look up and display their info: ")

    # Perform search
    print(mycontacts.get(name, "That name is not found."))


# This adds a new entry in the dictionary
def add(mycontacts):
    # Get the contact info
    name = input("Name: ")
    studentID = input("StudentID: ")
    GPA = input("GPA: ")
    grade = input("Expected Grade: ")
    status = input("Status (full-time or part-time: ")

    # Create a Contract Object name entry
    entry = student.Student(name, studentID, GPA, grade, status)

    # if name is not in the dictionary already, add it as a key with
    # entry object as the associated value
    if name not in mycontacts:
        mycontacts[name] = entry
        # this writes it to the dat file (to solve the lookup problem
        save_contacts(mycontacts)
        print("The entry has been added and saved to the student data file.")
        
    else:
        print("That name already exists.")

# This allows for changing of an existing dictionary entry
def change_gpa(mycontacts):
    # Get a name to look up in the dictionary
    name = input("Enter a name: ")

    if name in mycontacts:
        # Get a new phone number
        phone = input("Enter a new phone number: ")

        # Get a new email address
        email = input("Enter a new email address: ")

        # create a contact object name entry
        entry = contact.Contact(name, phone, email)

        # update the entry
        mycontacts[name] = entry
        print("Infomation has been added.")

    else:
        print("That name was not found.")

def change_grade(mycontacts):
    # Get a name to look up in the dictionary
    name = input("Enter the student's name you want to change: ")

    if name in mycontacts:
        # Get a new expected grade
        grade = (input("Enter a new expected grade here: "))

        # keep the same info for everything else

        # create a contact object name entry
        entry = student.Student(name, studentID, GPA, grade, status)

        # update the entry
        mycontacts[name] = entry
        print("Infomation has been added.")

    else:
        print("That name was not found.")


# This prints all student data that was written to the student_data.dat file 
def print_all():
    end_of_file = False
    input_file = open('student_data.dat', 'rb')
    while not end_of_file:
        try:
            studentdata = pickle.load(input_file)
            display_data(studentdata)
        except EOFError:
            end_of_file = True
    input_file.close()

def display_data(studentdata):
    print("Name: ", studentdata['name'])
    print("StudentID: ", studentdata['studentID'])
    print("GPA: ", studentdata['GPA'])
    print("Grade: ",studentdata['grade'])
    print("Status: ",studentdata['status'])
          



# This saves(pickles) the objects and saves it to the contact files
def save_contacts(mycontacts):
    # open the file for writting
    output_file = open(FILENAME, 'wb')

    # pickle the dictionary and save it
    pickle.dump(mycontacts, output_file)

    # close the file
    output_file.close()


# Call that sweet main
main()


    
    



        
