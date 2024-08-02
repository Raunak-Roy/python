# Maximum of two numbers Using lambda function
a = int(input("enter first number: "))
b = int(input("enter second number: "))

maxx_num = lambda a,b: a if a>b else b
print(f'{maxx_num(a,b)}, is the max number')

#Maximum of two numbers Using list comprehension

x = 23
y = 11

z = (x if x > y else y)
print(z, "is the max number of :", "{} and {}".format(x,y))