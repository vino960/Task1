import math

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def factorial_of_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    factorials = [math.factorial(fib) for fib in fib_sequence]
    return factorials

# Example usage:
n = 10  # Number of Fibonacci numbers
fib_sequence = fibonacci_sequence(n)
factorials = factorial_of_fibonacci(n)

print("Fibonacci Sequence:", fib_sequence)
print("Factorials of Fibonacci Sequence:", factorials)
