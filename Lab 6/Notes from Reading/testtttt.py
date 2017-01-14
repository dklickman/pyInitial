# This program will convert numeric values to a string value before
# writting them to a file.

def main():
    # open a new file to test with
    outfile = open('numbers.txt', 'w')

    # Get three numbers from the user
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    num3 = int(input("Number 3: "))

    # Write those numbers to a file
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file
    outfile.close()
    print("You data has been written.")

# Call the main function
main()

                  
            
