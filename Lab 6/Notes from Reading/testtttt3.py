def main():
    # open that file up for reading 
    emp_file = open('employees.txt', 'r')

    # create a variable that can be targeting by the while loop for
    # line reading
    name = emp_file.readline()
    
    while name != '':

        # Read the ID field
        id_num = emp_file.readline()

        # Read the dept
        dept = emp_file.readline()

        # Strip the newlines from the fields
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the records
        print("Name: ", name)
        print("ID: ", id_num)
        print("Dept: ", dept)

        name = emp_file.readline()

    # After the loop dies because of an empty string
    # We need to close the file
    emp_file.close()


# Call that sweet sweet main
main() 
