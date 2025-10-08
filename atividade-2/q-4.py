def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")

    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        raise ValueError("The list must contain at least two distinct numbers.")
    
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

nums = [10, 5, 8, 20, 20, 3]
result = second_largest(nums)
print(result)
