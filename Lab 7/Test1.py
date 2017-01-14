
def main():
    print("Here goes nothing.")
    table_temperatures()
    

def table_temperatures():
    #Create the two lists to be merged inside the 2D list
    fahrenheit_temps = list(range(-10, 110, 10))
    celcius_temps = [] 

    # Creates a Nested List 
    temperature_list = [[fahrenheit_temps],
               [celcius_temps]]


    index = 0
    while index < len(fahrenheit_temps):
        celcius_pull = (fahrenheit_temps[index] - 32) * (5 / 9)
        celcius_temps.insert(index,(format(celcius_pull, '.0f')))
        index += 1

    print("Here is a table to indicate the relative temperature.")
    print("Fahrenheit temps are the first row.")
    print("Celsius Temperatures are in quotes on the second.")
    print()
    print(temperature_list)


main()


