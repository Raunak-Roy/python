L = [1,2,3,4,5,6,7,8,9,10]
blank = []
for i in L:
    if i % 2 == 0:
        blank.append(i)
        for i in blank:
            blank.append(i**2)

print(blank)

x = [i**2 for i in L if i%2==0]
print(x)
