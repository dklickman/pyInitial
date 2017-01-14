# Using the readlines method, this program will return a file's
# contents as a list of strings.  Each line in the file will be an
# item in that list.  In our case our sourcefile was writting with \n
# characters, so we will need to strip them.

# This program reads a file's contents into a list
def main():
    # Open the file for reading
    infile = open('cities.txt', 'r')

    # Read the contents of the file into a list
    cities = infile.readlines()

    # Close the file
    infile.close()

    # Strip the \n from each of the elements
    # Create a counter to stop the reading
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # Print the list with the \n striped
    print(cities) 

# Call the main function
main() 
