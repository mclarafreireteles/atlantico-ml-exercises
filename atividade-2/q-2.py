def filter_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    
    return prime_numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = filter_primes(nums)
print(result)