def sum(a,b):
    return a+b
print(sum(4,5))
#sum of Two Numbers


#even or odd
def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_odd(15))  



#largest number
# def largest(a,b):
#     if a >b:
#         return a
#     return b
# print(largest(10,25))


#factorial 
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):  #1 6
#         fact *= i  #fact 1 *= 1  =1
#     return fact

# print(factorial(5))    

# def is_prime(num):
#     if num <= 1:
#         return False
    
#     for i in range(2,num):
#         if num % i ==0:
#             return False
        
#     return True
# num = int(input("enter number:"))

# if is_prime(num):
#     print("prime number")
# else:
#     print("not prime number")     


#swap two numbers

def swap(a,b):
    a,b = b,a
    print(a,b)
swap(10,20)   


#count digits
def count(num):
    return len(str(num))
print(count(12345))


#square
def square(num):
    return num*num
    # return num**3
print(square(12))