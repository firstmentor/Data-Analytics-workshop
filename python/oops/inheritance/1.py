class Test:
    def __init__(self, x):
        self.x = x

    def __str__(self): #object ko human readable format me print karne ke liye
        return f"Value is {self.x}"    

    
t=Test(5)
print(t)
#Ye useless memory address dikhata hai
# <__main__.Test object at 0x000001>







# Example with __str__()
# class Test:
#     def __init__(self, x):
#         self.x = x

#     def __str__(self):
#         return f"Value is {self.x}"

# t = Test(5)
# print(t)
# Ab readable output mila
# __str__() = object ko human readable format me print karne ke liye
# __init__ Python ka constructor hota hai