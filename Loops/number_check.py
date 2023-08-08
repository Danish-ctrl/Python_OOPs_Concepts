"""
Write a program that checks if a given number is positive, negative, or zero.
"""

n = int(input('Enter any number: '))
if n > 0:
    print(f"Number '{n}' is positive")
elif n < 0:
    print(f"Number '{n}' is negative")
else:
    print(f"Number is {n}")