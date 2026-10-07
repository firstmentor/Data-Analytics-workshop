class Employee:
    pub= 8
    _protec = 100
    __private ="vikas" 

   # __private =10
    def display(self):
        print(self.__private)

#access modifiers
a = Employee()
print(a.pub)
print(a._protec)
a.display()
# print(a.__private)

