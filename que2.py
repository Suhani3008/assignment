#. Write a python program that checks whether a given number is even or
#odd

number = int(input("Enter the number : "))

if number%2==0:
    print("The number {} is EVEN.".format(number))

else:
    print("The number {} is ODD.".format(number))