# This program will store multiple records inside of a file

def main():
    # Get the number of employees that need records created
    num_emps = int(input("How many employee records do you want " \
                         "to create? "))

    # Open a file for writing to
    emp_file = open("employees.txt", 'w')

    # Get each employees data and write it to the file

    for count in range(1, num_emps + 1):
        # print the primer statement so the user knows what's coming
        print("Enter data for employee: " , count)

        # create the varables that will be written to disk
        name = input("Employee Name: ")
        id_num = (input("ID number: "))
        dept = input("Department: ")

        # write those variables to the emp_file.txt file
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()
    emp_file.close()

    # let the user know that files have been successfully writen
    print("Employee records have been updated.")

        
# Call that sweet sweet main
main()
