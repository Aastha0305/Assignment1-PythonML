import string
def remove_punctuation(str):
    # Create an empty list to store non-punctuation characters
    no_punct = []
    # Iterate through each character in the input string
    for char in str:
        # Check if the character is not a punctuation character
        if char not in string.punctuation:
            # Add the character to the list
            no_punct.append(char)
    # Join the list into a string and return it
    return ''.join(no_punct)


str = input("Enter a string: ")
ans = remove_punctuation(str)

print("String without punctuation:")
print(ans)

