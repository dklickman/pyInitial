
num_date = input("Please enter a date in mm/dd/yy format: ")

# Create a variable to check against the month conditions
# and convert to an integer so we can math on it

month_check = int(num_date[0:1])
while month_check < 1 or month_check > 12:
    print("That is not a valid month, please re-enter the date.")
    num_date = input("Please enter a date in mm/dd/yy format: ")

day_check = int(num_date[3:4]
