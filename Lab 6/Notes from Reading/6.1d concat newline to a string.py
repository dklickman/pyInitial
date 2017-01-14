# This program gets three name from the user
# and writes them to a file.

def main():
    # Get three names.
    print("Enter the names of three friends: ")
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    # Open a file named friends.txt
    myfile = open('friends.txt', 'w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Close the file
    myfile.close()
    # Issue a statement on what just happened
    print('The names were written to friends.txt')
    
# Call the main function
main()
