#we can use the mrthods and attributes of Employee in Programmer object. Also we can overwrite or add new attributes and methods in programmer class.

class papa:
    car =  "bmw"

    def showDetails(self):
        print("This is an employee")

class ram:
    language = "Pyhton"
    #company ="google"

    def getLanguage(self):
        print(f"The language is {self.language}")


    # def showDetails(self):
    #     print("This is an Programmer")    


# e = papa()
# e.showDetails()
p = ram()
# p.getLanguage()
# p.showDetails()
print(p.car)
#p.showDetails()
#print(p.company)

#multiple