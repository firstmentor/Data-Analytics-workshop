# F(0)=0

# F(1)=1

# F(n)=F(n-1)+F(n-2)

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


for i in range(10):
    print(fibonacci(i), end=" ")