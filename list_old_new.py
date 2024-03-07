# Create a list of 10 strings
old_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'peach', 'pear', 'plum', 'lemon']

# Make a copy of the list
new_list = old_list.copy()

# Take input from the user for the positions to insert new elements
position1 = int(input("Enter the position for the first new element: "))
position2 = int(input("Enter the position for the second new element: "))

# Take input from the user for the new elements
new_element1 = input("Enter the first new element: ")
new_element2 = input("Enter the second new element: ")

# Insert the new elements at the specified positions in the new list
new_list.insert(position1, new_element1)
new_list.insert(position2, new_element2)

# Print the old and new lists
print("Old list:", old_list)
print("New list:", new_list)
