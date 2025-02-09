import random
import string

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices() to pick a random combination of characters
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

# Example of generating a random password of 12 characters
print(generate_password(12))
