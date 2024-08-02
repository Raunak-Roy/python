Listt = [2,4,5,7,9,2]

total = 0

for element in range(0, len(Listt)):
    total = total+Listt[element]

print(total)

s = sum(Listt)
print(s)

Listt = [2,4,5,7,9,2]
x = [i for i in Listt]
print(sum(x))