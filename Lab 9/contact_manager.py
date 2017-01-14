# This program manages contacts (aka students for the lab)

import contact 
import pickle

# Globals to be used for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constants for file name
FILENAME = 'contacts'

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

        elif choice == CHANGE:
            change(mycontacts)

        elif choice == DELETE:
            delete(mycontacts)

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
    print("(1) Look up a contact.")
    print("(2) Add a new contact.")
    print("(3) Change an existing contact.")
    print("(4) Delete a contact.")
    print("(5) Quit")

    # Get user choice
    choice = int(input("Enter your choice: "))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a menu item number."))
    return choice


# This looks up an item in a certain dictionary
def look_up(mycontacts):
    # Get the name to look up
    name = input("Enter a name to look up: ")

    # Perform search
    print(mycontacts.get(name, "That name is not found."))


# This adds a new entry in the dictionary
def add(mycontacts):
    # Get the contact info
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    # Create a Contract Object name entry
    entry = contact.Contact(name, phone, email)

    # if name is not in the dictionary already, add it as a key with
    # entry object as the associated value
    if name not in mycontacts:
        mycontacts[name] = entry
        print("The entry has been added.")
    else:
        print("That name already exists.")

# This allows for changing of an existing dictionary entry
def change(mycontacts):
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


# This allows for deletion of a specific dictionary item
def delete(mycontacts):
    # Get a name
    name = input("Enter a name: ")

    # if the name is found, delete it
    if name in mycontacts:
        del mycontacts[name]
        print("Entry deleted.")
        
    else:
        print("That name was not found.")


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


    
    



        
