#Write a python program that takes a list of numbers and returns their sum.

numbers = input("Enter a list of numbers separated by spaces: ")

number_list = [int(num) for num in numbers.split()]

sum_of_numbers = sum(number_list)


print("The sum of the numbers is:", sum_of_numbers)
