# Student Menu Constants
look_and_print = 1
add_student = 2
change_GPA = 3
change_grade = 4
print_all_student = 5
quit_choice = 6



def main():
    choice = 0
    while choice != quit_choice:
        # give user a menu to choose from 
        show_menu()

        choice = int(input("Enter the menu number view and modify students: "))
        # this will execute the choice as passed
        menu_choice(choice)
        print() 

            
#Menu to display options
def show_menu():
    print("Student Option Menu:")
    print()
    print("(1) Look up and print the student GPA")
    print("(2) Add a new student to the class")
    print("(3) Change GPA of student")
    print("(4) Change expected grade of student")
    print("(5) List all student data")
    print("(6) None (quit)")
    print()

# Match the choice to the functions and pass the value on 
def menu_choice(choice):
    if choice == look_and_print:
        print() 
        print("Please enter the Student's name.")
        print() 
        
    elif choice == add_student:
        print()
        print("Please add the student info: ")
        
        
    elif choice == change_GPA:
        print()
        print("Which Student's GPA would you like to change? ")
        print("Enter the new GPA.")        

    elif choice == change_grade:
        print()
        print("Which Student's expected grade would you like to change?")
        print("Enter the new expected grade.")        
    
    elif choice == print_all_student:
        print() 
        print("Here is all of the student info.")

    elif choice == quit_choice:
        print()
        print("We'll get you out of here.")
        exit()

    else:
        print("Invalid Selection")

# Call the main
main()
