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
            main()

               

        
        

        print("END it worked")



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

# Match the choice to the functions
def menu_choice(choice):
    if choice == M_T_K:
        
        

    elif choice == G_T_L:
        print("number 2")   
        

    elif choice == P_T_K:
        print("number 3")

    elif choice == I_T_C:
        print("number 4")

    elif choice == F_T_C:
        degrees_fahrenheit = float(input('How many degrees Fahrenheit'  \
        'need to be converted to Celsius? '))
        FahToCel(degrees_fahrenheit)
        print()

    elif choice == quit_choice:
        print("We'll get you out of here.")
        exit()

    else:
        print("Invalid Selection")


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
    count = 0
    for count in range(10):
        con_out_file = open('conversionsoutput.txt', 'a')
        print(degrees_fahrenheit, "Fahrenheit")
        print("Is equal to",format(result, '.2f'), "Celcius")
        con_out_file.write(str(degrees_fahrenheit) +  '\n')
        con_out_file.write(str("fahrenheit"))
        con_out_file.write(str(result) + '\n')
        con_out_file.write(str("celcius" + '\n'))
        con_out_file.close()
        count += 1 
    












main()
    
