# def find_duplicates(nums):
#     # Your code here
#
# # Example usage:
# print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 5]))  # Output should be [1, 2, 5]
value = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 5]
dupl = []
for i in value:
    value.append(i)
    if i in dupl:
        value.pop()

print(value)