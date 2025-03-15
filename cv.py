def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_two_digit_primes():
    primes = []
    for num in range(10, 100):  # Check numbers between 10 and 99 (inclusive)
        if is_prime(num):
            primes.append(num)
    return primes

# Calling the function and printing the result
two_digit_primes = find_two_digit_primes()
print("Prime numbers with 2 digits are:", two_digit_primes)
