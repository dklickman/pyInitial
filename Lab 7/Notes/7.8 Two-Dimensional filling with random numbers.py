# This program assigns a random numbers to a two-dimensional list

# Lol, don't forget to import the random module dummy
import random

# Constants for rows and columns
ROWS = 3
COLS = 4

def main():
    # Create a 2D list
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    
    # Fill the list with random numbers
    # which is saying because we need three rows we need this outer loop
    # to iterate 3 times ^^ look up at constant variable for why 3
    for r in range(ROWS):
        # this is saying because we need four columns we need this inner loop
        # to iterate 4 times creating 4 columns
        for c in range(COLS):
            # this puts a random number in the r and c indexs in the list
            values[r][c]= random.randint(1,100)

    # display the random numbers
    print(values)

    print("You can also use a nested loop to print a single list out of the 2d.")
    for r in range(ROWS):
        for c in range(COLS):
            print(values[r][c])

# Call the main
main()
            
