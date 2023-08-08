"""
Create a program that generates the Fibonacci sequence
up to a given number of terms)
"""


def fibonacci(first_num, second_num, num):
    print('Fibonacci series are: ')
    print(first_num, second_num, end=' ')
    for i in range(1, num-1):
        next_number = first_num + second_num
        first_num = second_num
        second_num = next_number
        print(next_number, end=' ')


first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
n = 10
fibonacci(first, second, n)