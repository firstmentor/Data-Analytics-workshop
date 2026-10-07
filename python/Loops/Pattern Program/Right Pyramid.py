n = 5

for i in range(1, n + 1):  #1  5

    print(" " * (n - i), end="")  #" " * (5-1) = " "*4 = "    " " " * (5-2) = " "*3 = "   "
    for j in range(i): # 0 1
        print("*", end=" ")

    print()

