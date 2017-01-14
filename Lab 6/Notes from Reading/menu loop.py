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
        show_menu()
        try:
            choice = int(input("Enter the menu number to perform a conversion: "))
        except ValueError:
            print("ERROR! You must enter a number.")
            print()
            main()
            
        if choice == M_T_K:
            print("test made it")

        
        
        





# Menu to display options
def show_menu():
    print("Conversion Menu")
    print("(1) Miles to Kilometers")
    print("(2) Gallons to Liters")
    print("(3) Pounds to Kilograms")
    print("(4) Inches to Centimeters")
    print("(5) Fahrenheit to Celsius")
    print("(6) None (quit)")
    print()


    
main()
    
