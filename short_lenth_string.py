# Take input for the number of elements in the list
N = int(input("Enter the number of elements: "))

# Initialize an empty list to store the strings
string_list = []

# Take input for the strings and append them to the list
for i in range(N):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

# Sort the list based on the length of strings
sorted_list = sorted(string_list, key=len)

# Print the sorted list
print("Sorted list based on length of strings:", sorted_list)
