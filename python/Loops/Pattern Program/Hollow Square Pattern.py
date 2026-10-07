n = 5

for i in range(n): # 0 4
    for j in range(n): # 0 1 2 3 4

        if i == 0 or i == n-1 or j == 0 or j == n-1: # 0==0 or 0==4 or 0==0 or 0==4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()