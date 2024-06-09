def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase for a case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    
    return sorted_str1 == sorted_str2

# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
