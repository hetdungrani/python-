# Create a list of strings
my_list = ['apple', 'banana', 'orange', 'grape', 'banana', 'kiwi', 'banana']
print(my_list)
# Take input from the user for the string to search
search_string = input("Enter a string to search in the list: ")

# Count how many times the specified string is present in the list
count = my_list.count(search_string)

# Print the count
print(f"The string '{search_string}' is present {count} times in the list.")
