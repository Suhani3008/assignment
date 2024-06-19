#Write a python program that removes all punctuation from a given string.


import string

string1 = input("Enter a string: ")


str = ''.join(char for char in string1 if char not in string.punctuation)

print("String without punctuation:",str)
