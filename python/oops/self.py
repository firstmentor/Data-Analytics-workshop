# self refers to the insatnce of the class 
# It is automatically passed with a function call 
# from an object.
class  Employee:
    company = "pninfosys"
    def getSalary(self,a):  #automatic pass parameter
        print("Salary is 100k")
        print(f"Salary is {self.salary}")
        print(f"Salary is {self.salary}")
        print(f"Salary is this employee working in {self.company} is {self.salary}")

rohit = Employee()
rohit.salary =100000
rohit.getSalary(3000) #Employee.getsalary(rohit)



