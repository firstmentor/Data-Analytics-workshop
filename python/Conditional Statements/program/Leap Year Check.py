year = int(input("Enter Year: "))
#366 2024 ,2000
#2023 not leap year
if (year % 400 == 0) or (year % 4 ==0 and year % 100 !=0):
    print("Leap Year")
else:
    print("Not Leap Year")