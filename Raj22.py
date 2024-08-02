Liss = [2,5,7,8,10, 1, 3, 6, 11,12]
evenvalue = []
for i in Liss:
    if i%2 == 0:
        evenvalue.append(i)
    else:
        print(i)
print(evenvalue)

x = [i for i in Liss if i%2 == 0]
print(x)

m = [[2,3,4,5,6], [4,6,8], [9,8,5,2]]
print([i for j in m for i in j])