def count_characters(str):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Iterate over each character in the string
    for char in str:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1

    return char_count

str = input("Enter a string: ")
char_frequency = count_characters(str)

print("Character frequency:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")
