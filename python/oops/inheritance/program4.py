class student:
    def __init__(self , name , marks, password):
        self.name = name #pub
        self._marks = marks #pro
        self.__password = password #pri

    #public method
    def display(self):
        print("name : " , self.name)
        print("marks : " , self._marks)

    #private method
    def __check_password(self):
        print("password : " , self.__password)

    #public method to access private method    
    def login(self):
        self.__check_password()    

class result(student):
    def grade(self):
        if self._marks >= 90:
            print("Grade : A")
        elif self._marks >= 80:
            print("Grade : B")
        elif self._marks >= 70:
            print("Grade : C")
        elif self._marks >= 60:
            print("Grade : D")
        else:
            print("Grade : F")

#object creation
s = result("rahul" , 90 , "1234")
s.display()    
s.grade()    
s.login()    

        

        