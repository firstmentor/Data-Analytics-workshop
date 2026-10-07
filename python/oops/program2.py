class programmer:
    company  = "Pninfosys"
    def __init__(self, name ,product):
        self.name = name
        self.product = product
   
    def getInfo(self):
        print(f"The name of the {self.company}programmer is {self.name} and the product is {self.product}") 

        

rohit = programmer("rohit","github")
# vikas = programmer("vikas","google")     
rohit.getInfo()
# # vikas.getInfo()  
rohit.name="raj" 
rohit.getInfo()          