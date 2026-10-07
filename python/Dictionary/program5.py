numbers ={10,20,30,40,50}
print("set: ",numbers)

#add element
numbers.add(60)
print("After add:",numbers)

#remove element using discard
numbers.discard(50)
print("After discard:",numbers)

#pop
numbers.pop()
print("After pop:",numbers)

if 20 in numbers:
    print("20 is present in the set")
else:
    print("20 is not present in the set")

#union
set_a={1,2,3}
set_b={3,4,5}
print("Union:",set_a.union(set_b))

#intersection
print("Intersection:",set_a.intersection(set_b))