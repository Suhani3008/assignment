#Write a python program that calculates the factorial of a given number

print("Calculating Factorial ->")

number = int(input("Enter the number : "))

factorial = 1

for i in range(1,number+1):
    factorial*=i

print("The Factorial of {} is {}.".format(number,factorial))