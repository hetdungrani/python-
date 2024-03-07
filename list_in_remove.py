def remove_vowels(word):
    word = word.lower()

    char_list = []

    for char in word:
        if char not in ('a', 'e', 'i', 'o', 'u'):
            char_list.append(char)

    return char_list

word_input = input("Enter a word: ")

result_list = remove_vowels(word_input)
print(f"List of characters without vowels: {result_list}")
