print("Convert Miles to Kilometers.")

miles_to_convert = float(input("How many miles need to be converted? "))

#validate the number
while miles_to_convert < 0:
    miles_to_convert = float(input("Number needs to be positive: "))
    while miles_to_convert < 0:
        miles_to_convert = float(input("Last Chance: "))
        while miles_to_convert < 0:
            #this will terminate program
            exit()
    
m_to_km = miles_to_convert * 1.6
user_name = input("Please enter your name: ")
user_email = input("What is your e-mail address? ")
while "@" not in user_email:
    print("Please enter a valid e-mail to include the '@' address.")
    print("How else would send e-mail spam to you?")
    user_email = input("Please re-enter your e-mail address? ")
print("Thank you", user_name, "for updating your e-mail to", user_email)
print('That many miles is equal to', format(m_to_km, '.1f'), 'Kilometers.')

#
#
#

### get the temperature (f) from user
degrees_fahrenheit = float(input('How many degrees Fahrenheit need to be converted to Celsius? '))

# insert validation loop for range of realistic range of temperatures
while degrees_fahrenheit > 1000:
    degrees_fahrenheit = float(input('Please keep the temperature under 1000, my computer can\'t count that high: '))
    while degrees_fahrenheit > 1000:
        degrees_fahrenheit = float(input('Last chance to enter a value under 1000 degrees fahrenheit: '))
        while degrees_fahrenheit > 1000:
            exit()
          
f_2_c = ( degrees_fahrenheit - 32) * (5 / 9)
user_name = input("Please enter your name: ")
user_email = input("What is your e-mail address? ")
while "@" not in user_email:
    print("Please enter a valid e-mail to include the '@' address.")
    print("How else would send e-mail spam to you?")
    user_email = input("Please re-enter your e-mail address? ")
print("Thank you", user_name, "for updating your e-mail to", user_email)
print('That is', format(f_2_c, '.0f'), 'degrees Celsius.')

#
#
#

### convert gallons to liters
gallons = float(input('How many Gallons need to be converted to Liters? '))

# input validation against negative gallons
while gallons < 0:
    print("Can't convert negative gallons.")
    gallons = float(input("You have 2 attempts remaining for a valid entry: "))
    while gallons < 0:
        gallons = float(input("Last Chance to enter a number > 0: "))
        while gallons < 0:
            exit()
    
liters = gallons * 3.9
user_name = input("Please enter your name: ")
user_email = input("What is your e-mail address? ")
while "@" not in user_email:
    print("Please enter a valid e-mail to include the '@' address.")
    print("How else would send e-mail spam to you?")
    user_email = input("Please re-enter your e-mail address? ")
print("Thank you", user_name, "for updating your e-mail to", user_email)
print('That would be', format(liters, '.1f'), 'Liters.')

#
#
#

### convert pounds to kilograms
pounds = float(input('How many Pounds need to be converted into Kilograms? '))

# check 
while pounds < 0:
    print("Negative pounds are for diets, not conversion programs.")
    pounds = float(input("Enter a positive value for weight: "))
    while pounds < 0:
        pounds = float(input("1 attempt remaining: "))
        while pounds < 0:
            exit()
    
kilo = pounds * .45
user_name = input("Please enter your name: ")
user_email = input("What is your e-mail address? ")
while "@" not in user_email:
    print("Please enter a valid e-mail to include the '@' address.")
    print("How else would send e-mail spam to you?")
    user_email = input("Please re-enter your e-mail address? ")
print("Thank you", user_name, "for updating your e-mail to", user_email)
print('That would be', format(kilo, '.2f'), 'Kilograms.')

#
#
#

### convert inch to centimeter
inch = float(input('How many Inches need to be converted to Centimeters? '))
while inch < 0:
    print("You cannot enter negative values: ")
    inch = float(input("How many Inches need to be converted to Centimeters? "))
    while inch < 0:
        inch = float(input("Last Chance: "))
        while inch < 0:
            print("Maximum amount of attempts, closing program.")
            exit()

cm = inch * 2.54

user_name = input("Please enter your name: ")
user_email = input("What is your e-mail address? ")
while "@" not in user_email:
    print("Please enter a valid e-mail to include the '@' address.")
    print("How else would send e-mail spam to you?")
    user_email = input("Please re-enter your e-mail address? ")
print("Thank you", user_name, "for updating your e-mail to", user_email)

print('That would be', format(cm, '.2f'), 'Centimeters.')



print("Working with this lab makes me appreciate functions.")



### END ### 


















