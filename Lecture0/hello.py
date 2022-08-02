#Ask user for their name
name = input("Name? ")

#Say hello to user
print("Hello,", name, sep="...", end="!\n")

"""
This is a comment
"""

#Don't jump to newline
print("Hello, ", end="")

#Add a . before newline
print(name, end=".\n")

#f-String
print(f'Hi, {name}')

#Trim whitespaces from input string
name = name.strip()
print(name)