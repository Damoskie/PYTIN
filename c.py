import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # The computer randomly selects a number between 1 and 100.
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Prompt the user to guess a number.
            user_guess = int(input("Make a guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid number.")

# Call the game function
number_guessing_game()
