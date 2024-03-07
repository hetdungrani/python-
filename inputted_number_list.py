# Take input for the number of elements in the list
N = int(input("Enter the number of elements: "))

# Initialize an empty list to store the numbers
numbers_list = []

# Iterate N times to get N user inputted numbers
for i in range(N):
    number = int(input(f"Enter number {i+1}: "))  # Convert input to float for flexibility
    numbers_list.append(number)  # Append the inputted number to the list

# Print the final list
print("List of inputted numbers:", numbers_list)
