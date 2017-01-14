# this program reads and displays the contents
# of the philosophers.txt file

def main():
    # Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read the file's contents one at a time
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()


    #Close the file
    infile.close()

    # Print the data that was read into
    print(line1,line2,line3)
    

# Call the main
main()
