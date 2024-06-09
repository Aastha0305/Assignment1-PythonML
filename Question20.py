def calculate_sum(numbers):
    
    total = 0
    for num in numbers:
        total += num
    
    return total


numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
total_sum = calculate_sum(numbers)
print("The sum of the numbers is:", total_sum)
