# Function to swap three numbers
def swap_three_numbers(a, b, c):
    # Swap the numbers using a temporary variable
    a, b, c = c, a, b
    return a, b, c

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Swapping the numbers
num1, num2, num3 = swap_three_numbers(num1, num2, num3)

# Display the swapped values
print(f"After swapping: \nFirst number: {num1}\nSecond number: {num2}\nThird number: {num3}")
