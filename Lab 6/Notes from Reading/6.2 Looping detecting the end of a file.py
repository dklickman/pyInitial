def main():
    sales_file = open('sales.txt.', 'r')

    for line in sales_file:
        #convert to float
        amount = float(line)
        # format and display the amount
        print(format(amount, '.2f'))

    sales_file.close()

main()
