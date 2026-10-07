# Set Python ka ek collection data type hai jo unique values store karta hai.

# Duplicate values automatically remove ho jati hain.
# Indexing nahi hoti.
# Unordered collection hai (items ka order fixed nahi hota).
# Mutable hai (add/remove kar sakte hain).

# numbers = {10, 20, 30, 20, 10}
# print(numbers)  # 20 10 30 (order change ho sakta hai) Duplicate Values Allowed Nahi Hai
# numbers.add(40)
# print(numbers)  # 20 10 30 40 (add karta hai)Mutable Hai
# print(numbers[0])  #index nahi hota




# Empty Set Banana
# s = { }  #dictionary hai ❌
# s = set()  #set hai ✅
# print(type(s))



# Set Mein Item Add Karna
# add()
# fruits = {"Apple", "Mango","ram"}

# fruits.add("Banana")
# fruits.add("abc")
# fruits.update(["ravi", "mohit"])
# fruits.remove("Apple123")
# fruits.discard("Orange") #remove (Error Nahi Deta)
# fruits.pop() #remove
# fruits.clear() #remove all items

# print(fruits)




# # Loop in Set
fruits = {"Apple", "Mango", "Banana"}
# print(fruits)

for fruit in fruits:
    print(fruit)