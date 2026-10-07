def hello(n):
    if n == 0:
        return   #ab function ruk gaya 

    print("Start", n)      # start 2  start 1

    hello(n-1)  #hello(1) #hello(0)

    print("End", n)

hello(2)