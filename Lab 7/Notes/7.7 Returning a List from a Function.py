# This program uses a function to create a list
# The function returns a reference to the list

def main():
    # Get a list with values stored in it
    numbers = get_values()

    # Display the values in the list
    print("The numbers are", numbers)


# The get_values() function gets a series of numbers
# from the user and stores them in a list where the
# function returns a reference to the list

def get_values():
    # Create an empty list to fill
    values = []

    # Create a variable to control the loop
    again = 'y'

    # Get the values from the user and add them
    # to the list
    while again == 'y' or again == 'Y':
        num = int(input("Enter a number: "))
        values.append(num)

        # Prompt user to enter another value
        # or exit the loop
        again = input("Enter 'y' to enter another number.")

    # return the list
    return values

# Call that sweet sweet main
main()

        
