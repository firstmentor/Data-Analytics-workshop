class bikeShop:
    #stock = 100
    def __init__(self,stock):
        self.stock=stock
        # print(self.stock)
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the postive value or greater the zero")
        elif q>self.stock:
            print("enter the value (less the stock)")
        else:
            self.stock =self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)   
while True:
    obj =bikeShop(100)
    uc =int(input('''
1 Display Stock
2 Rent a Bike
3 Exit
        ''' ))
    if uc ==1:
        obj.displayBike()
    elif uc == 2:
        n =int(input("Enter qty"))
        obj.rentForBike(n)
    else:
        break    



                      


