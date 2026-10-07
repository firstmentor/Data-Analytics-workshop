from abc import ABC, abstractmethod

class Car(ABC): #abstract class
    @abstractmethod
    def start(self):#abstract method
        pass

class BMW(Car):
    def start(self):  
        print("car started")


car1= BMW()
car1.start()
