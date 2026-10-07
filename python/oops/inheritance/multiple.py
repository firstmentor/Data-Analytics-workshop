class Employee:
    car  = "pninfosy" 
    ecode   =120

class Freelancer:
    car = "google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):
    #car="abcd"
    name= "vikas"
    
 
p = Programmer()
print(p.car)
p.upgradeLevel()
print(p.level)