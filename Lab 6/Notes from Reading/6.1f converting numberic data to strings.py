# This program will convert numeric data types to string values
# before they are written to a text file

def main():
    # Open (in this case create) a file for writing
    outfile = open('numbers.txt', 'w')

    # Get three numbers from the user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))

    # Write the numbers to a file - we want to
    # convert them using str first though
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file
    outfile.close()

    # Indicate the data was written
    print("The data has been written to numbers.txt")

# Call the main
main()

               
