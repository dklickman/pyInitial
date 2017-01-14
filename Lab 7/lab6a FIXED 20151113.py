# Global Constants / Earth-bound laws of physics
convert_miles_to_km = 1.6
convert_gallons_to_liters = 3.9
convert_pounds_to_kg = .45
convert_inches_to_cm = 2.54

# Menu Constants
M_T_K = 1
G_T_L = 2
P_T_K = 3
I_T_C = 4
F_T_C = 5
quit_choice = 6



def main():
    choice = 0
    while choice != quit_choice:
        # give user a menu to choose from 
        show_menu()

        # exception handler
        try:
            choice = int(input("Enter the menu number to perform a conversion: "))
            menu_choice(choice)

            
        except ValueError:
            print("ERROR! You must enter a number.")
            print()
            # give user another chance to enter numberic value
            

         

# Menu to display options
def show_menu():
    print("Conversion Menu:")
    print()
    print("(1) Miles to Kilometers")
    print("(2) Gallons to Liters")
    print("(3) Pounds to Kilograms")
    print("(4) Inches to Centimeters")
    print("(5) Fahrenheit to Celsius")
    print("(6) None (quit)")
    print()

# Match the choice to the functions and pass the value on 
def menu_choice(choice):
    if choice == M_T_K:
        count = 0
        while count < 10:
            miles_to_convert = float(input("How many miles need to be converted? "))
            milesToKm(miles_to_convert)
            count += 1
            print()
        
    elif choice == G_T_L:
        count = 0
        while count < 10:            
            gallons = float(input('How many Gallons need to be converted to Liters? '))
            GalToLit(gallons)
            count += 1
            print()            
        
    elif choice == P_T_K:
        count = 0
        while count < 10:
            pounds = float(input('How many Pounds need to be converted into Kilograms? '))
            PoundsToKg(pounds)
            count += 1
            print()

    elif choice == I_T_C:
        count = 0
        while count < 10:
            inch = float(input('How many Inches need to be converted to Centimeters? '))
            InchesToCm(inch)
            count += 1
            print()
            
    elif choice == F_T_C:
        count = 0
        while count < 10:
            
            degrees_fahrenheit = float(input('How many degrees Fahrenheit'  \
            'need to be converted to Celsius? '))
            FahToCel(degrees_fahrenheit)
            count += 1
            print()

    elif choice == quit_choice:
        print("We'll get you out of here.")
        exit()

    else:
        print("Invalid Selection")



##### Conversion Functions #####

# Do the conversion, print text of last submitted input and write the results to the text file (with loop)
def milesToKm(miles_to_convert):
    # validation loop for a positive distance traveled
    while miles_to_convert < 0:
        miles_to_convert = float(input("Enter a positive value. "))
        while miles_to_convert < 0:
            miles_to_convert = float(input("Last chance to enter a positive value. "))
            while miles_to_convert < 0:
                exit()

    result = miles_to_convert * convert_miles_to_km
    con_out_file = open('conversionsoutput.txt', 'a')
    print(miles_to_convert, 'miles is equal to', format(result, '.1f'), 'Kilometers.')
    con_out_file.write(str(miles_to_convert) +  '\n')
    con_out_file.write(str("Miles" + '\n'))
    con_out_file.write(str(result) + '\n')
    con_out_file.write(str("Kilometers" + '\n'))
    con_out_file.close()
    

# Do the conversion, print text (with loop), and write the results to the text file (with loop) 
def GalToLit(gallons):
    # validate number is positive 
    while gallons < 0:
        gallons = float(input("Enter a positive amount of gallons to convert. "))
        while gallons < 0:
            gallons = float(input("Last chance to enter a positive amount of gallons to convert. "))
            while gallons < 0:
                exit()                
    liters = gallons * convert_gallons_to_liters
    con_out_file = open('conversionsoutput.txt', 'a')
    print(gallons, 'Gallons is equal to', format(liters, '.1f'), 'Liters.')
    con_out_file.write(str(gallons) +  '\n')
    con_out_file.write(str("Gallons" + '\n'))
    con_out_file.write(str(liters) + '\n')
    con_out_file.write(str("Liters" + '\n'))
    con_out_file.close()
        
# Do the conversion, print text (with loop), and write the results to the text file (with loop)
def PoundsToKg(pounds):
    # validate pounds are positive 
    while pounds < 0:
        pounds = float(input("Please enter a positve value. "))
        while pounds < 0:
            pounds = float(input("Last chance to enter a positve value. "))
            while pounds < 0:
                exit()
    kilo = pounds * convert_pounds_to_kg
    con_out_file = open('conversionsoutput.txt', 'a')
    print(pounds, 'pounds is equal to', format(kilo, '.1f'), 'kilograms.')
    con_out_file.write(str(pounds) +  '\n')
    con_out_file.write(str("Pounds" + '\n'))
    con_out_file.write(str(kilo) + '\n')
    con_out_file.write(str("Kilograms" + '\n'))
    con_out_file.close()
        

# Do the conversion, print text (with loop), and write the results to the text file (with loop)  
def InchesToCm(inch):
    # validate inches are positive
    while inch < 0:
        inch = float(input("Enter a positive number. "))
        while inch < 0:
            inch = float(input("Last chance to enter a positive number. "))
            while inch < 0:
                exit()
    cm = inch * convert_inches_to_cm
    con_out_file = open('conversionsoutput.txt', 'a')
    print(inch, 'inches is equal to', format(cm, '.2f'), 'centimeters.')
    con_out_file.write(str(inch) +  '\n')
    con_out_file.write(str("Inches" + '\n'))
    con_out_file.write(str(cm) + '\n')
    con_out_file.write(str("Centimeters" + '\n'))
    con_out_file.close()
  
    
# Do the conversion, print text (with loop), and write the results to the text file (with loop)
def FahToCel(degrees_fahrenheit):
    # validation loop to ensure realistic temps are being entered
    while degrees_fahrenheit > 1000:
        degrees_fahrenheit = float(input('Re-enter a temperature under 1000: '))
        while degrees_fahrenheit > 1000:
            degrees_fahrenheit = float(input('Last change to re-enter a temperature under 1000: '))
            while degrees_fahrenheit > 1000:
                exit()
        
    result = ( degrees_fahrenheit - 32) * (5 / 9)
    con_out_file = open('conversionsoutput.txt', 'a')
    print(degrees_fahrenheit, "Fahrenheit")
    print("Is equal to",format(result, '.2f'), "Celcius")
    con_out_file.write(str(degrees_fahrenheit) +  '\n')
    con_out_file.write(str("fahrenheit"))
    con_out_file.write(str(result) + '\n')
    con_out_file.write(str("celcius" + '\n'))
    con_out_file.close()
         
    

# Call the main function
main()
    
