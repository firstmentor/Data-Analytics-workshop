
class papa:
    bike =  "007"

    def showDetails(self):
        print("This is an employee")

class son(papa):  #inherits the attributes and methods of papa class
    language = "Pyhton"
    #bike ="008"

    def getLanguage(self):
        print(f"The language is {self.language}")
    # def showDetails(self):
    #     print("This is an Programmer")    
p = son()
print(p.bike)
p.showDetails()
p.getLanguage()
