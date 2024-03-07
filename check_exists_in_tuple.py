def check_item_existence(my_tuple, item_to_check):
    return item_to_check in my_tuple

my_tuple = (1, 2, 3, 4, 5)

item_to_check = int(input("Enter an item to check in the tuple: "))

if check_item_existence(my_tuple, item_to_check):
    print(f"The item {item_to_check} exists in the tuple.")
else:
    print(f"The item {item_to_check} does not exist in the tuple.")
