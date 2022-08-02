#Integer calculation
x = int(input("What's x? "))
y = int(input("What's y? "))

print("Result: ", x + y)

#Float calculation
a = float(input("What's a? "))
b = float(input("What's b? "))

"""
#Round off the result to 2 significant digits after the floating point
c = round(a / b, 2)


#Insert a comma separator
print(f'{c:,}')
"""

c = (a / b)

#Round off the result to 2 significant digits after the floating point
print(f'{c:.2f}')

"""
x = (input("What's x? "))
y = (input("What's y? "))

#Convert string input to integer type utilizing 'int' function
z = int(x) + int(y)

print(z)
"""