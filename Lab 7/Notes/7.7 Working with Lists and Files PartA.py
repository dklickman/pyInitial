# This program uses the writelines method to save a list of strings
# to a file

def main():
    # Create a list
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open / create a file to write to
    outfile = open('cities.txt', 'w')

    # Write the list to the file
    outfile.writelines(cities)

    # Close the file
    outfile.close()

# Call the main
main()
