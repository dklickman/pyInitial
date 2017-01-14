# Teacher drops the lowest grade at the end of the semester for all exams
# taken.  Write a program that will capture students grades in a list
# and then destroy the lowest grade

# Get the students test score
# Calculate the total of the scores
# Find the lowest score
# Subtract the lowest score from the total.  This gives the adjusted total
# Divide the adjusted total by 1 less than the number of test scores (avg)
# Display the average

def main():
    # Get the test score from the user using a function
    scores = get_scores()

    # Get the total of the test scores
    total = get_total(scores)

    # Get the lowest score
    lowest = min(scores)

    # Subtract the lowest score from the total
    total -= lowest

    # Calculate the average.  Note the / by total - 1
    # due to the fact we killed the lowest score
    average = total / (len(scores) - 1)

    # Display the average
    print("The average of test scores minus the lowest is: ", average)

# This function will capture the test scores from the user
# and return the value to the scores variable in main()
def get_scores():
    # Create an empty list for user to fill
    test_scores = []

    # Create a variable to control the loop
    again = 'y'

    # Get the scores from the user
    # and add them (append) to a list
    while again == 'y':
        # Get the score and add it to the list
        value = float(input("Enter a test score: "))
        test_scores.append(value)

        # Want to hit that shit again?
        again = input("Enter 'y' to enter another test score")
        print()

    # return the list of values to the get scores function
    # which in turn assigns that value to the scores in main
    return test_scores

# This function accepts a list as an argument returns the total
# of the values in the list
def get_total(value_list):
    # Create a variable to use as an accumulator
    total = 0.0

    # Calculate the total of the list elements
    for num in value_list:
        total += num

    # return the total
    return total

# Call that sweet sweet main
main()

    
    
    
