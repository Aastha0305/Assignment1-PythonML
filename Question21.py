def count_occurrences(lst, target):
    
    count = 0
    for element in lst:
        if element == target:
            count += 1
    
    return count

lst = [1, 2, 2, 3, 2, 4, 5, 2]
target = int(input("Enter the element to count occurrences for: "))
ans = count_occurrences(lst, target)
print(f"The element {target} occurs {ans} times in the list.")
