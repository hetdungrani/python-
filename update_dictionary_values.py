def update_dictionary_values(input_dict):
    for key in input_dict:
        new_value = input(f"Enter a new value for '{key}': ")
        input_dict[key] = new_value

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

update_dictionary_values(my_dict)

print("Updated dictionary:", my_dict)
