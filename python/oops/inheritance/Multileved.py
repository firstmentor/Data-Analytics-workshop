class Person:
    conuntry = "India"

    def takeBreath(self):
        print("gwalior")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
            super().takeBreath()
            print("pninfosys") 

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):

        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Progarmmer so I am Luckily breathing++...")    

p = Programmer()
p.takeBreath()
