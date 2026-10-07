# Jab hume pehle se pata ho ki loop kitni baar chalega, 
# tab hum for loop use karte hain.

# for variable in sequence:
#     code


fruits = ["Apple", "Mango", "Banana"] #list
# # print(fruits)

# for f in fruits:
#     print(f)

# i = 0
# while i < len(fruits): #3
#     print(fruits[i])
#     i +=1




# print(len(fruits))


# For Loop Kab Use Karte Hain?

# Jab hume pehle se pata ho loop kitni baar chalega.


# for i in range(5):
#     print(i)



# range() Function

# range() numbers ki sequence generate karta hai.

# for i in range(5):  # 0 4 start stop
#     print(i) #0 1 2 3 4


# for i in range(1, 6): #Stop value include nahi hoti.
#     print(i)

# # range(start, stop, step)
# for i in range(1, 11, 2):   #Yahan step = 2 hai, matlab 2-2 ka jump.
#     print(i)

# # Reverse Loop
# for i in range(10, 0 , -1):  # -1 ka matlab reverse direction.
#     print(i)


# Strings ko iterate karna
# for c in "vikas jain":    #String is a sequence of characters.
#     print(c)


# List Par Loop

#List ke har item ko access karne ke liye loop use karte hain.

fruits = ["Apple", "Mango", "Banana"] #list


for f in fruits:
    print(f)

print(len(fruits)) 


i = 0
while i < len(fruits):
    print(fruits[i])
    i +=1