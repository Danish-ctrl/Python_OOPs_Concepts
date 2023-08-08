"""
 Implement a program that finds the largest number in a list.
"""

l = [1, 2, 3, 45, 65, 21]
k = []

print(max(l))

print('Another method using loop')
# Initialize a variable to store the largest number
largest = l[0]

# Iterate through the list to compare each element
for num in l:
    if num > largest:
        largest = num

print("The largest number is:", largest)
