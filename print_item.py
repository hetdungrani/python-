def print_items_in_range(my_tuple, start_index, end_index):
    selected_items = my_tuple[start_index:end_index + 1]
    return selected_items

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

start_index = 2  
end_index = 4    
selected_items = print_items_in_range(my_tuple, start_index, end_index)

print(f"The items in the range {start_index} to {end_index} are: {selected_items}")

