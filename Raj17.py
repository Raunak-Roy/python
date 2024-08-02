# find max and min


listt = [33, -44, 55, 22, 13, 67, 98, 23, 77, 34]

maxvalue = 0

for element in listt:
    if element > maxvalue:
        maxvalue = element

print("the maximum value is :",maxvalue)

minvalue = 0
for i in listt:
    if i < minvalue:
        minvalue = i
print("minimum value is as mentioned below: ", minvalue)


