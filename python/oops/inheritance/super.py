class Person:
    conuntry = "India"

    def __init__(self):
        super().__init__()
        print("Initializing Person...\n")

    def takeBreath(self):

        print("I am breathing....")
class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing em...\n")

    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
        #super().takeBreath()
        print("I am an Employee so I am Luckily breathing...") 

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        #super().takeBreath()
        print("I am an Progarmmer so I am Luckily breathing++...")    

# p = Person()
# p.takeBreath()
# e = Employee()
# e.takeBreath()
pr = Programmer()
pr.takeBreath()