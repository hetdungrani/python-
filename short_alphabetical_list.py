# Take input for the number of elements in the list
N = int(input("Enter the number of elements: "))

# Initialize an empty list to store the strings
string_list = []

# Take input for the strings and append them to the list
for i in range(N):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

# Sort the list in alphabetical order
string_list.sort()

# Print the sorted list
print("Sorted list in alphabetical order:", string_list)
