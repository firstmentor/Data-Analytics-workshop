class student:
    __name ="ravi"   #private varibale direct object ke sath use nahi hota hai...

    def __init__(self):   #Constructor ki help se call kar sakate hai
        print(self.__name)
        self.__displayinfo()

    def __displayinfo(self): #PRIVATE 
        print("hello gwalior")

    def itm(self):
        self.__displayinfo()   
        print(self.__name)

obj =student()
# print(obj.__name)
obj.itm()



#Encapsulation getter and setter
class Stduents:
    def __init__(self):
        self._name =""

    def getname(self):
        return self._name

    def setname(self,name):
        self._name =name

obj =Stduents()
obj.setname("raj")
# obj.setname("kumar")
name = obj.getname()
print(name)                