def convert_case(input_string):
    result_string = input_string.swapcase()
    return result_string

user_input = input("Enter a string: ")

converted_string = convert_case(user_input)
print("Converted string:", converted_string)
