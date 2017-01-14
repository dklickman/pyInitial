# You can also use a loop to write lists one element at a time

def main():
    # Create a list of strings
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open / Create a file for writting
    outfile = open('cities.txt', 'w')

    # Write the list to the file
    for item in cities:
        outfile.write(item + '\n')

    # Close the file
    outfile.close()

# Call the main
main()
