def filter_odds(numbers):
    odd_numbers = []
    
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    
    return odd_numbers

nums = [1, 2, 3, 4, 5, 6, 7]
result = filter_odds(nums)
print(result) 