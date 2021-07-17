import re

#Class to model User
class User:

    #User constructor
    def __init__(self ):
        
        self._name = ""
        self._company = ""
        self._email = ""
        self._telephone = ""
        self._password = ""
        self._locked = True
    
    #Attribute Getters
    @property
    def name(self):
        return self._name
    def company(self):
        return self._company
    def email(self):
        return self._email
    def telephone(self):
        return self._telephone
    def password(self):
        return self._password
        
    
    #Setters

    @name.setter
    def name(self, other_name):

        #If there is no White space : Just one part id provided
        if " " in other_name == False:
            print("Please provide a Name and a First Name !")
        
        else:
            self._name = other_name
    

    def company(self, other_company):
        self._company = other_company
    
    
    def email(self, other_email):
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        #For regular expression pattern

        if re.match(regex, other_email):
            self._email = other_email
        else:
            print("Please provide a valid email !")
    
    
    def telephone(self,other_telephone):

        #Check if Phone Number is valid
        #test if it begins by zero, contains 10 digits

        pattern = re.compile("(0)?[0-9]'){10}")

        #If it matches : valid phone
        if pattern.match(other_telephone):
            self._telephone = other_telephone
        else:
            print("Please provide a valid phone number !")
        
    def set_password(self, password):
        self._password = password

    def validate_password(self, password):

        if self._password == password:
            self._locked = False
            return True
        
        return False
        

















        









    

    
