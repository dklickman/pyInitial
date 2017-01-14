# import the class module

import part1lab9

def main():
    # Get the info for the student
    stu_name = input("Enter the student name: ")
    stu_ID = input("Enter the studentID: ")
    stu_GPA = input("Enter the student GPA: ")
    stu_grade = input("Enter the student's expected grade: ")
    stu_status = input("Is the student full-time(enter FT) or part-time(enter PT)? ")

    student_object = part1lab9.Student(stu_name, stu_ID, stu_GPA, stu_grade, stu_status)

    print("Here is the student data: ")
    print(student_object.get_name())


main()
    
