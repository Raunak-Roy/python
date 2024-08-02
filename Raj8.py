#Find the Factorial of a Number Using Recursive approach


def getfact(n):
    return 1 if (n==1 ) or (n ==0) else n*getfact(n-1)

c  = getfact(4)
print(c)


def check(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n*check(n-1)
result = check(9)
print(result)

