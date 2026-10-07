# Agar key na mile to error nahi aata.

student = {
    "name": "Ravi",
    "age": 21,
    "city":"gwl"
}
# print(student["phone"])
print(student.get("phone"," Not Found"))
student["city"] = "Ahmedabad"  # add
student["age"] = 25  # update
student.pop("age") # remove
student.clear()
print(student)





