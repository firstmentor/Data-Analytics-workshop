#Operators in Python can be overloaded usering dunder methods.
#these methods are called when a given  operator used on the objects.
class Number:
    def __init__(self,num ):   #dunder methods
        self.num = num
        print(num)
        
    def __add__(self,a):
        #print(a.num)
        return self.num  + a.num
        


    # def __mul__(self, num2):
    #     print("Lets add")
    #     return self.num * num2.num 

    # def __truediv__(self, num2):
    #     print("Lets add")
    #     return self.num / num2.num           
    
    # def __floordiv__(self, num2):  
    #     print("Lets add")
    #     return self.num // num2.num 


    # def __str__(self):
    #     return f"Decimal Number: {self.num}"    

n1 = Number(4)
n2 = Number(6)
# print(n1)
# print(n2)
sum = n1 + n2
print(sum)
# mul =n1 * n2
#print(sum)
# print(mul)



# n1 = Number(10)
# print(n1)
