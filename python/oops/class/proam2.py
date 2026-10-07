class Calculator:
    
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square is {self.n * self.n}")

    def cube(self):
        print(f"the square is {self.n * self.n * self.n }")        


a =Calculator(2)  
a.square()
a.cube()     

    