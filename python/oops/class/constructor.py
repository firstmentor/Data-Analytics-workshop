
# --init--() is a special method 
class Employee:
    name = "pninfosys"
    salary =20000

   

    def __init__(self,name,salary,lan): #dunder method which is automatically called
       self.name  =name
       self.salary = salary
       self.lan = lan
       print("I am obj")
    def  team():
      print("")  


    def pn(self):
       print(f"the lanua is {self.lan}.the salary is {self.salary}")
          
data = Employee("viki",12000,"java") #object
print(data.name,data.salary)
data.pn()
    
      