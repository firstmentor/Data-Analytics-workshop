student ={
    "name":"ram",
    "age":34,
    "course":"pyhton"
}

print("student Infotmation")
print("Name :",student["name"])
print("Age :",student["age"])
print("Course :",student["course"])


for key,value in student.items():
    print(key, ":", value)