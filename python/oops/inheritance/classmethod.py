# A class method is a method which is bound to the class and not
#the project of the class. @classmethod docorator is used to create a class method
class Employee:
    company = "pninfosys"
    salary =100 
    location  = "Delhi"
    
    def change(self):
        print(f"hello {self.location}")

    @classmethod
    def changeSalaery(a, sal):
        a.salary = sal 
        print(f"hello {a.salary}")
       

e  = Employee()
print(e.salary)
# e.change()
e.changeSalaery(5000)
print(e.salary)
print(Employee.salary)


