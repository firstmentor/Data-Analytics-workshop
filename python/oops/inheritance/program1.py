# class C2dvec:
#     def __init__(self, i , j):
#         self.icap =i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"  

# class C3dvec(C2dvec): 
#     def __init__(self, i , j,k):
#         super().__init__(i,j)
#         self.Kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.Kcap}k" 


# v2d = C2dvec(1,3)
# v3d = C3dvec(1,9, 7)
# print(v2d)
# print(v3d)                


# polymorphism
# ek hi function ko diffrent different tarah se use karna
# 1. compile time polymorphism
# 2. run time polymorphism

# print(len("pninfosys"))
# print(len([1,2,3,4,5]))
# print(len({1:"a", 2:"b", 3:"c"}))

#overriding

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# a =Animal()
# b =Dog()

# a.sound()
# b.sound()

# class Bird:
#     def fly(self):
#         print("Bird flies")

# class Eagle(Bird):
#     def fly(self):
#         print("Eagle flies high")

# b =Bird()
# e =Eagle()

# b.fly()
# e.fly()

#overloading
#python me overloading nhi hota hai
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

#     def add(self, a, b, c, d):
#         return a + b + c + d

# calc = Calculator()
# print(calc.add(1, 2))
# print(calc.add(1, 2, 3))
# print(calc.add(1, 2, 3, 4))

