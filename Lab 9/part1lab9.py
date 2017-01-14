# Create the Student class

class Student:
    # initialize the attribute
    # pass the attributes that are needed in addition to self
    def __init__(self, name, studentID, GPA, grade, status):
        self.__name = name
        self.__studentID = studentID
        self.__GPA = GPA
        self.__grade = grade
        self.__status = status
            

    # create a method to accept an argument for name
    def set_name(self, name):
        self.__name = name

    # create a method to accept an argument for studentID
    def set_studentID(self, studentID):
        self.__studentID = studentID

    # create a method to accept an argument for GPA
    def set_GPA(self, GPA):
        self.__GPA = GPA

    # create a method to accept an argument for grade
    def set_grade(self, grade):
        self.__grade = grade

    # create a method to accept an argument for status
    def set_status(self, status):
        self.__status = status


    # return the student name
    def get_name(self):
        return self.__name
    
    # return the studentID
    def get_studentID(self):
        return self.__studentID
    
    # return the GPA
    def get_GPA(self):
        return self.__GPA
    
    # return the grade
    def get_grade(self):
        return self.__grade
    
    # return the status
    def get_stutus(self):
        return self.__status
    

