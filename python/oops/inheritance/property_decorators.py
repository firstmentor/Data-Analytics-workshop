# class Employee:
#     company = "pninfosys"
#     salary =  5600
#     salarybonus = 300
    


#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus


#     def totalSalary(self):
#         return self.salary + self.salarybonus
        

# e = Employee()
# print(e.totalSalary)
# print(e.totalSalary())






















class Employee:
    company = "pninfosys"
    salary =  5600
    salarybonus = 400


    @property
    def totalSalary(self):
        return self.salary + self.salarybonus



    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary  
        

e = Employee()
print(e.totalSalary)
e.totalSalary=7000
print(e.salary)
print(e.salarybonus)
