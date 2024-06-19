#Write a python program that generates the first n numbers in the Fibonacci sequence.


n = int(input("Enter the value of n : "))

fibonacci_numbers = [0, 1]

for i in range(2, n):
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_number)

print("First", n, "numbers in Fibonacci sequence:", fibonacci_numbers)
