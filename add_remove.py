def add_element(my_list, new_element):
    my_list.append(new_element)

def remove_element(my_list, element_to_remove):
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
    else:
        print(f"The element '{element_to_remove}' is not in the list.")

my_list = [1, 2, 3, 4, 5]

new_element = int(input("Enter a new element to add to the list: "))
add_element(my_list, new_element)
print("List after adding the new element:", my_list)

element_to_remove = int(input("Enter an element to remove from the list: "))
remove_element(my_list, element_to_remove)
print("List after removing the specified element:", my_list)
