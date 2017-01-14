
# Global Constants / Earth-bound laws of physics
convert_miles_to_km = 1.6
convert_gallons_to_liters = 3.9
convert_pounds_to_kg = .45
convert_inches_to_cm = 2.54


# build the main module for execution
def main():
    # Part A that converts miles to kilometers
    miles_to_convert = float(input("How many miles need to be converted? "))
    milesToKm(miles_to_convert)
    print()

    # Part B that converts Fahrenheit to celsius
    degrees_fahrenheit = float(input('How many degrees Fahrenheit'  \
    'need to be converted to Celsius? '))
    FahToCel(degrees_fahrenheit)
    print()

    # Part C that converts gallons to liters
    gallons = float(input('How many Gallons need to be converted to Liters? '))
    GalToLit(gallons)
    print()

    # Part D that converts pounds to kilograms
    pounds = float(input('How many Pounds need to be converted into Kilograms? '))
    PoundsToKg(pounds)
    print()

    # Part E that converts inches to centimeters
    inch = float(input('How many Inches need to be converted to Centimeters? '))
    InchesToCm(inch)
    print()

    
# PART A ||| Function that converts miles to kilometers
def milesToKm(miles_to_convert):
    # validation loop for a positive distance traveled
    while miles_to_convert < 0:
        miles_to_convert = float(input("Enter a positive value. "))
        while miles_to_convert < 0:
            miles_to_convert = float(input("Last chance to enter a positive value. "))
            while miles_to_convert < 0:
                exit()
    result = miles_to_convert * convert_miles_to_km
    print(miles_to_convert, 'miles is equal to', format(result, '.1f'), 'Kilometers.')
    return

# PART B ||| Function that converts Fahrenheit to Celcius
def FahToCel(degrees_fahrenheit):
    # validation loop to ensure realistic temps are being entered
    while degrees_fahrenheit > 1000:
        degrees_fahrenheit = float(input('Re-enter a temperature under 1000: '))
        while degrees_fahrenheit > 1000:
            degrees_fahrenheit = float(input('Last change to re-enter a temperature under 1000: '))
            while degrees_fahrenheit > 1000:
                exit()
        
    result = ( degrees_fahrenheit - 32) * (5 / 9)
    print('That is', format(result, '.0f'), 'degrees Celsius.')
    return


# PART C ||| Function that converts Gallons to Liters
def GalToLit(gallons):
    # validate number is positive 
    while gallons < 0:
        gallons = float(input("Enter a positive amount of gallons to convert. "))
        while gallons < 0:
            gallons = float(input("Last chance to enter a positive amount of gallons to convert. "))
            while gallons < 0:
                exit()                
    liters = gallons * convert_gallons_to_liters
    print('That would be', format(liters, '.1f'), 'Liters.')
    return

        
# PART D ||| Function that converts Pounds to Kilograms
def PoundsToKg(pounds):
    # validate pounds are positive 
    while pounds < 0:
        pounds = float(input("Please enter a positve value. "))
        while pounds < 0:
            pounds = float(input("Last chance to enter a positve value. "))
            while pounds < 0:
                exit()
    kilo = pounds * convert_pounds_to_kg
    print('That would be', format(kilo, '.2f'), 'Kilograms.')
    return

# PART E ||| Function that converts Inches to Centimeters
def InchesToCm(inch):
    # validate inches are positive
    while inch < 0:
        inch = float(input("Enter a positive number. "))
        while inch < 0:
            inch = float(input("Last chance to enter a positive number. "))
            while inch < 0:
                exit()
    cm = inch * convert_inches_to_cm
    print('That is', format(cm, '.2f'), 'Centimeters.')
    return


#Call the function to execute
main()

