class pn:
    name ="ram"  #this is a class Attribute
    city ="walior"
    salary =400000

    def mpct(self,a): #objct pass
        print(f"my name {self.name}. The salary is {self.salary} {a}")
         
    def itm(self):
        print("hllo walior")

    @staticmethod
    def mits(a,b):
        print("hello",a+b) 
        # print("hello")
        #print(f"my name {self.name}. The salary is {self.salary}")   


data =pn()
# data.mpct(20)
#pn.mpct(data) //convert
#data.itm()
data.mits(3,4)


