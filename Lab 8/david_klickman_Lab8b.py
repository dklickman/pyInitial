
date_string = input("Please enter a date in mm/dd/yy format: ")
# Split the date by the way of '/'
date_list = date_string.split('/')

month_check = int(date_list[0])
day_check = int(date_list[1])
year_check = int(date_list[2])

# Ensures month is in range
while month_check < 1 or month_check > 12:
    print("That is not a valid month value.")
    date_string = input("Please enter a date in mm/dd/yy format: ")
    date_list = date_string.split('/')
    month_check = int(date_list[0])

# Ensures day is in range
while day_check < 1 or day_check > 31:
    print("That is not a valid day value.")
    date_string = input("Please enter a date in mm/dd/yy format: ")
    date_list = date_string.split('/')
    day_check = int(date_list[1])

# Ensures the year 2013 is the only year accepted
# this also satisfies 2 digits long as the only correct way
# to get out of the loop is to enter 13 for the year value
while year_check != 13:
    print("This program only accepts the year 2013 in 'yy' format.")
    date_string = input("Please enter a date in mm/dd/yy format: ")
    date_list = date_string.split('/')
    year_check = int(date_list[2])

if month_check == 1:
    month_spelled == "January"
elif month_check == 2:
    month_spelled = "February"
elif month_check == 3:
    month_spelled = "March"
elif month_check == 4:
    month_spelled = "April"
elif month_check == 5:
    month_spelled = "May"
elif month_check == 6:
    month_spelled = "June"
elif month_check == 7:
    month_spelled = "July"
elif month_check == 8:
    month_spelled = "August"
elif month_check == 9:
    month_spelled = "September"
elif month_check == 10:
    month_spelled = "October"
elif month_check == 11:
    month_spelled = "November"
elif month_check == 12:
    month_spelled = "December"
    
print("Your date in long form is: ", month_spelled, " ",day_check,", 2013", sep='')


