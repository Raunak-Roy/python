#list comprehension

#set comprehension
#dictionary comprehension
nums = [2, 4, 6, 4, 7, 8, 8, 9, 11, 22]

evenn = []
oddd = []
# for i in nums:
#     sq.append(i*i)
for i in nums:
    if i%2==0:
        if i%3==0:
            oddd.append(i*i*i)
        evenn.append((i*i))

print("even value os here:", evenn)
print("od value is here: ", oddd)

#list compreghension me kya hoga

# x = [i*i for i in nums]
# print(x)
xx = [i*i*i==0 for i in nums]
print(xx)