def main():
    # Open a file name philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # write the names of the philosophers to file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file
    outfile.close()

# call the main function

main()
