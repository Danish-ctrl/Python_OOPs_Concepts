"""
Create a function to count the number of vowels in a
given string.
"""


def vow_count(input_word, word_list, count):
    for i in input_word:
        if i in word_list:
            count += 1
        else:
            continue

    print(f'Vowel count in string "{input_word}" is: {count}')


counter = 0
l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
word = input('Enter a string: ')
vow_count(word, l, counter)
