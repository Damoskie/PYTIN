def rightmost_set_bit(n):
    if n == 0:
        return None  # No set bits in 0
    return n & -n

# Test the function
number = int(input("Enter a number: "))
result = rightmost_set_bit(number)

if result is None:
    print("The number has no set bits.")
else:
    print(f"The rightmost set bit is at position: {result}")
