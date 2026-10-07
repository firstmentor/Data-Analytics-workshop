#creating instance attribute salary for both the object
class Employee:
    company  = "pninfosys"
    salary =100


rahul = Employee()
rohit = Employee()
rahul.salary = 400       #instance attribute
rohit.salary = 500
rohit.company="ram"
print(rahul.salary)        #class attribute
print(rohit.salary)
print(rohit.company)    #error 
