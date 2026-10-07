# String characters ka collection hota hai.
# String immutable hota hai.
name = "pninfosys"
# 0 1  2 3 4 5 6 7 8
# P N  I N F O S Y S


# print(name)
# print(name[0])  #0 12
# print(name[1])

# name[0]="J" # string is immutable,therefore we can't change the value of string
# print(name)  # TypeError: 'str' object does not support item assignment

name = name + "Softwares"
print(name)   # Concatenation


# Slicing

# name = "PNINFOSYS"
# # 0 1  23
# # -1 -2 -3

# print(name[0:4])  #start with 0 and end with 3
# print(name[4:7])  #start with 4 and end with 6
# print(name[:])  # All characters
# print(name[:7]) # First 7 characters
# print(name[4:]) # From index 4 to end
# print(name[-3:]) # Last 3 charactersl
# print(name[::-1]) # Reverse the string
# print(name[0:9]) # From index 0 to last 2 characters



# Useful String Methods
# name ="pninfosys"

# print(len(name)) 
#print(name.upper()) # Convert to uppercase
# print(name.lower()) # Convert to lowercase
# print(name.count("n")) # Count occurrences of a character
# print(name.find("n")) # Find the index of a character
# print(name.replace("n", "X")) # Replace a character
# print(name.strip()) # Remove leading/trailing whitespace
# print(name.split()) # Split the string into a list
# name1 = ["pninfosys", "is", "er"]
# print(name.join(name1)) # Join a list into a string
# print(name.title()) # Convert to title case
# print(name.capitalize())
