# creating a function for addition of two numbers

def addnum(a,b):
    if a == 0:
        return b
    else:
        return a+b

a = int(input("enter first number: "))
b = int(input("enter second numbers: "))
check = addnum(a,b)
print(check)