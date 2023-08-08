"""
Given a list of numbers, find the sum and average
"""
l = [1, 2, 3, 4, 5]
summ = 0
for i in l:
    summ = summ + i

print(f"Sum is: {summ}")

length = len(l)

average = summ / length
print(f"Average is: {average}")