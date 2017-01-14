

# layout the main
def main():

    # Call the student input function    
    student_input()
    # Call the file checker
    file_name_check()
    # fin


def student_input():
    try:
        count = 0
        while count < 12:
            student_name = input("What is the student's name? ")
            grade = int(input("What is the student's average grade? "))
            if grade < 0 or grade > 100:
                print("Student grade must be between 0 and 100.")
                print("Resubmit the last student and grade.")
                student_input()
            else:
                # open (create) file and make it appendable
                grade_file = open('grades.txt', 'a')
                # write student name to grades.txt file
                grade_file.write(str(student_name) + '\n')
                # write student grade to grades.txt file
                grade_file.write(str(grade) + '\n')
                # close the file
                grade_file.close()                            
                print("File updated.")
                count += 1
                
    except ValueError:
        print("You must enter a numeric value between 0 and 100 " \
              "for the student grade.  Please begin again")
        grade_file = open('grades.txt', 'w')
        grade_file.close()
        main()


def file_name_check():
    try:
        check_grade_file = open('grades.txt', 'r')
        
        # Have the lines printed 
        for line in check_grade_file:
            print(line)
    except FileNotFoundError:
        print("The file needed for this operation cannnot be found.")
        print("Please replace or relocate 'grades.txt' it's original location.")
        

        
# Call the main
main()
