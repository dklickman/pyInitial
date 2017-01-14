# This is an example of how a number list can be writting to a file
# Note that the numbers must be converted to a string in order
# to be written and then the \n character is concatenated to it

def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Open / Create a file to write the numbers in
    outfile = open('numberlist.txt', 'w')

    # Write the list to the file * remember to convert to str
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Close the file
    outfile.close()

# Call the main
main()
