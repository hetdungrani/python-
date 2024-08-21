def reverse_number(number):
    reversed_str = str(number)[::-1]
    
    reversed_number = int(reversed_str)
    
    return reversed_number

number = int(input("Enter a number: "))

reversed_number = reverse_number(number)

print("Reverse of the number:", reversed_number)
