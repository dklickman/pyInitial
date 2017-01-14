
num_date = input("Please enter a date in mm/dd/yy format: ")

# Create variables to check against the month conditions
# and convert to an integer so we can math on it
month_check = int(num_date[0:2])
day_check = int(num_date[3:5])
year_first_value = (int(num_date[6]))
year_second_value = (int(num_date[7]))
year_check = year_first_value + year_second_value

print(month_check, day_check, year_check)

while month_check < 0 or month_check > 12:
    print("That is not a valid month, please re-enter the date.")
    num_date = input("Please enter a date in mm/dd/yy format: ")
    while day_check < 0 or day_check > 31:
        print("That is not within the range of a valid day of the month.")
        num_date = input("Please re-enter the date: ")
        while year_check != 4:
            print("2013 is the only valid year for entry in this program.")
            print()
            num_date = input("Please re-enter the date: ")
    

print("Fin")
