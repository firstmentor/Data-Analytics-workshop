#Operators in Python can be overloaded usering dunder methods.
#these methods are called when a given  operator used on the objects.
class Number:
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
        
n = Number(10)
print(n)        

    



    


