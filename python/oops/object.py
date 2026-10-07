#An object is an instantiation of a class.
#when class is defined, a template(info) is defined.
#Memory is allocated only after object instantion.


#object
# class itm1:
#   x = 5

#   def user(self,a,b):
#     print("hello user",a+b)

# p1 = itm1() #object
# # print(p1.x)
# p1.user(2,3) # 3 value




class pninfosys:
      comapnay ="pninfosys"
      age =12
      college ="ITM"

      def itm(self,a):
            print(f"Hello ITM {self.comapnay} is {self.age} is {self.college}\n{a}")
            print("hello",a)
           

data = pninfosys() #object
print(data.comapnay)
data.itm(2) #2 value



 




     



