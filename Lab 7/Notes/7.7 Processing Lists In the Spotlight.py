# Coffe shop with 6 employees.  All have the same payrate.
# Owner needs to have a program that provides the gross pay
# that needs to be paid to each worker for hrs worked

# use the num_employees as a constant to control the size
# of the list
num_employees = 6

def main():
    # Create a list to hold employee hours
    hours = [0] * num_employees
    total_hours = 0 

    # Get each employee's hours worked
    for index in range(num_employees):
        print("Enter the hours worked by employee", index + 1, \
                ": ", sep='', end='')
        hours[index] = float(input())
        total_hours += hours[index]

    # Get the hourly pay rate
    pay_rate = float(input("Enter the hourly payrate: "))

    # Display the employee's gross pay
    for index in range(num_employees):
        gross_pay = hours[index] * pay_rate
        print("Gross pay for employee", index + 1, ": $", \
              format(gross_pay, ',.2f'), sep='')
              
    print("Total Hours: ",total_hours)
# Call the main()
main()
