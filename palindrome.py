"""
Create a Python function to check if a given string is a
palindrome. Used 'reversed() method to get the elements in reverse order of the string
"""

s = input('Enter a string: ')
l = list(s)
k = []


def palindrome(l):
    for i in reversed(l):
        k.append(i)

    print('+++++')
    print(l)
    print(k)
    if k == l:
        print('Palindrome')
    else:
        print('not a palindrome')


palindrome(l)