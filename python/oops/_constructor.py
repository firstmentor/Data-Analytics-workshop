
# --init--() is a special method 

class Employee:
    company = "pninfosys"

    def __init__(self):
       print("vikas jain")
          

    def getDetails(self,name, salary):
        print(self.company)
        print(f"The name of the employee is name : {name}") 
        print(f"The name of the employee is salary:  {salary}")
     
rohit = Employee()  
# rohit = Employee()
rohit.getDetails('raj',1234)
      