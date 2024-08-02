#Python | Multiply all numbers in the list

Listt = [2,4,2,5,6]

def multiply(Listt):
    result = 1
    for x in Listt:
        result *= x
        return result

print(multiply(Listt))