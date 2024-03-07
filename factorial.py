def calculate_factorial(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

num_of_factorials = int(input("Enter the number of factorials to calculate: "))

i = 0
while i < num_of_factorials:
    num = int(input(f"Enter number {i + 1}: "))
    result = calculate_factorial(num)
    print(f"The factorial of {num} is: {result}")
    i += 1
