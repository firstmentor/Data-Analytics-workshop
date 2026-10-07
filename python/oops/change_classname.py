class Employee:
    company  = "pninfosys"
    salary =100


rahul = Employee()

print(rahul.company)
print(rahul.salary)
Employee.salary=1000
Employee.company ="google"
print(rahul.salary)
print(rahul.company)
