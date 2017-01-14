# the contact class holds contact information

class Contact:
    # __init__ method initializes the attributes
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # The set name method sets the name attribute
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    # The get name method returns the name attribute
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    # The __str__ method returns the objects state as string
    def __str__(self):
        return "Name: " + self.__name + \
               "\nPhone: " + self.__phone + \
               "\nEmail: " + self.__email
    
