convert_inch_to_cm = 2.54


def main():
    table_inch()


def table_inch():
    #Create the two lists to be merged inside the 2D list
    inch_list = list(range(0, 110, 10))
    cm_list = [] 

    # Creates a Nested List 
    length_list = [[inch_list],
                    [cm_list]]


    index = 0
    while index < len(inch_list):
        cm_pull = inch_list[index] * convert_inch_to_cm
        cm_list.insert(index, cm_pull)
        index += 1

    print("Here is a table to indicate relative length.")
    print("Inches are shown in the first row.")
    print("Centimeters are are shown in quotes on the second.")
    print()
    print(length_list)




main()
