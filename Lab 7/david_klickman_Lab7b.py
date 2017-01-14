# Chapter 7 Lab Part B


# Constant Variable for number of students for input
number_of_students = 12



def main():
    
    students = get_names()
    students = sorting_hat(students)
    students = prof_up_ender(students)
    students = narcissist(students)
    write_list(students)
    read_list() # shows contents of names.txt
    # convert to tuple
    students = tuple(students)
    
    
    

# list and name appender 
def get_names():
    name_list = []
    for num in range(number_of_students):
        name = input("Name of the student: ")
        name_list.append(name)
    return name_list

# Hogwarts 
def sorting_hat(students):
    students.sort()
    students.reverse()
    return students

# Adds professor's name to end of list
def prof_up_ender(students):
    students.append("Professor Polanco")
    return students

# Me, me, me, me
def narcissist(students):
    students.insert(0, "Dave")
    return students

# Writes the list to a text file ***with a \n due to .writelines***
def write_list(students):
    outfile = open('names.txt', 'w')
    for item in students:
        outfile.writelines(item + '\n')
    outfile.close()
    
# Reads the text file that contains the list ***Strip the \n***
def read_list():
    infile = open('names.txt', 'r')
    # read the file into memory
    student_list = infile.readlines()
    infile.close()

    # Strip the \n stored in the text file
    index = 0
    while index < len(student_list):
        student_list[index] = student_list[index].rstrip('\n')
        index += 1

    # Print the list
    print(student_list)
    
# Call the main 
main()
