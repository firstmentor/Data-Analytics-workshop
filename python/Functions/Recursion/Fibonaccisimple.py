# Fibonacci Series mein har naya number pichhle 2 numbers ka sum hota hai.
# 0 1 1 2 3 5 8 13 21 34 ...
# 0
# 1
# 0+1 = 1
# 1+1 = 2
# 1+2 = 3
# 2+3 = 5
# 3+5 = 8
# 5+8 = 13

n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c



# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")

#         c = a + b
#         a = b
#         b = c

# fibonacci(10)







# | a | b  | Print | c = a+b |
# | - | -- | ----- | ------- |
# | 0 | 1  | 0     | 1       |
# | 1 | 1  | 1     | 2       |
# | 1 | 2  | 1     | 3       |
# | 2 | 3  | 2     | 5       |
# | 3 | 5  | 3     | 8       |
# | 5 | 8  | 5     | 13      |
# | 8 | 13 | 8     | 21      |
