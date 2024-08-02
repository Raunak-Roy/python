#Python program to find second largest number in a list

x = [22,33,44,55,66,44,88,99]

xx = sorted(set(x))
print(xx[-2])

