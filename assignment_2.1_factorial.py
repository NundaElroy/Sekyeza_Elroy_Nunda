# Assignment 1: Find the factorial of 5

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Find factorial of 5
print(f"5! = {factorial(5)}")