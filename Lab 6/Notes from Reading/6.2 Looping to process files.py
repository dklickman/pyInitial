# This program prompts the user for sales amounts
# and wrties those amounts to the sales.txt file

def main():
    # Get the number of days
    num_days = int(input("Enter how many days do " + \
                         "you have sales: "))

    # Open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    # Get the amount of sales for each day and write
    # it to the sales.txt file.
    for count in range(1,num_days + 1):
        # Get the sales for a day
        sales = float(input("Enter the sales for day #" + \
                            str(count) + ": "))

        # Write the sales amount to the file.
        sales_file.write(str(sales) + "\n")

    # Close the file
    sales_file.close()
    print("Data written to sales.txt.")

# Call the main
main()

                    
        
