# *args Kya Hota Hai?

# *args ka matlab hai multiple positional arguments.

# Agar user kitni bhi values bheje, sab ek tuple ke andar store ho jati hain.

# def function_name(*args):
#     print(args)




def numbers(*args):
    print(args)

numbers(10, 20, 30)


# (10, 20, 30) Yahan args ek tuple hai.


# def total(*numbers):
#     print(sum(numbers))

# total(10, 20)
# total(10, 20, 30)
# total(10, 20, 30, 40)




# def students(*names):

#     for name in names:
#         print(name)

# students("Rahul", "Aman", "Riya", "Priya")





# Class me kabhi 10 students hote hain, kabhi 30.

# Hume pehle se nahi pata kitne students honge.

# def attendance(*students):

#     print("Total Students :", len(students))

# attendance("Rahul", "Aman")

# attendance("Rahul", "Aman", "Riya", "Priya")