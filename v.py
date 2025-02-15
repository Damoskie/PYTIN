import tkinter as tk
import random

# Function to get the computer's choice
def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# Function to update the result
def play_game(player_choice):
    comp_choice = computer_choice()
    result = ""
    
    # Determine the winner
    if player_choice == comp_choice:
        result = f"Both chose {player_choice}. It's a tie!"
    elif (player_choice == 'Rock' and comp_choice == 'Scissors') or \
         (player_choice == 'Paper' and comp_choice == 'Rock') or \
         (player_choice == 'Scissors' and comp_choice == 'Paper'):
        result = f"You win! {player_choice} beats {comp_choice}."
    else:
        result = f"You lose! {comp_choice} beats {player_choice}."
    
    # Update the result label
    result_label.config(text=result)

# Function to handle button press
def on_button_click(choice):
    play_game(choice)

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Adding instructions label
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instructions_label.pack()

# Creating buttons for each choice
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), width=20, command=lambda: on_button_click('Rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), width=20, command=lambda: on_button_click('Paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), width=20, command=lambda: on_button_click('Scissors'))
scissors_button.pack(pady=10)

# Adding label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Starting the Tkinter main loop
root.mainloop()
