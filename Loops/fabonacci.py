"""
Create a program that generates the Fibonacci sequence
up to a given number of terms)
"""

first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
n = 10
print('Fibonacci series are: ')
print(first, second, end=' ')
for i in range(1, n-1):
    next_number = first + second
    first = second
    second = next_number
    print(next_number, end=' ')
