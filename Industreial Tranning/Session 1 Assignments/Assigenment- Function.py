# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.

def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Error: The number must be a non-negative integer.")
        return None

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial_of_5 = factorial(5)
if factorial_of_5 is not None:
    print("Factorial of 5:", factorial_of_5)
