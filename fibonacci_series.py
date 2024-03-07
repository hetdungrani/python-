def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1

    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

num_of_fibonacci = int(input("Enter the number of Fibonacci numbers to generate: "))

result = fibonacci_series(num_of_fibonacci)
print(f"Fibonacci series of {num_of_fibonacci} numbers:", result)
