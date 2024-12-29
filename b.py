# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over each digit
    num_str = str(number)
    
    # Get the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Input from the user
user_input = int(input("Enter a number to check if it is an Armstrong number: "))

# Check if the input number is an Armstrong number
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
