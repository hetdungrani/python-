def count_occurrences(input_string, specified_value):
    occurrences = input_string.count(specified_value)
    return occurrences

user_input = input("Enter a string: ")
specified_value = input("Enter the specified value to count: ")

result_count = count_occurrences(user_input, specified_value)
print(f"The specified value '{specified_value}' appears {result_count} times in the string.")
