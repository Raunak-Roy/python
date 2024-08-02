#list comoprehension

listt = [2,4,5,6]
sroot = []

for i in listt:
    if i % 2 == 0:
        sroot.append(i*i)
    else:
        print("outside")


print(sroot)
#
# x = [i*i for i in listt]
# print(x)