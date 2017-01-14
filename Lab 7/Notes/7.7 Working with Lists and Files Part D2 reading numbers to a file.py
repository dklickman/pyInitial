# While reading numbers from a file into a list; convert the number
# stored as a string back into an integer so math can be performed

# This program reads numbers from a file into a list

def main():
    # Open the file
    infile = open('numberlist.txt', 'r')

    # Read the file's content into a list
    numbers = infile.readlines()

    # Close the file
    infile.close()

    # Create a loop to convert the string values stored in the
    # list into integers

    # Create an indexerror prevention variable 
    index = 0
    while index < len(numbers):
        # This says the value assigned to index is equal to the
        # element position in the list, then we convert that to an int
        numbers[index] = int(numbers[index])
        index += 1

    print(numbers)

    

# Call the main function
main()

