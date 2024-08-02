# #Find Maximum of two numbers in Python

a = 12
b = 24

print(max(a,b))

def maxx(a,b):
    if a > b:
        return a
    else:
        return b

c = maxx(12,4)
print(c)

#using ternary operator

x = 4
y = 7

print(x if x> y else y)

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print(a if a > b else b)
