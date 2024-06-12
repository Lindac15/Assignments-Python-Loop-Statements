# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.

import random  # Import the random module
items = ["ball", "paint brush", "puppy", "bow", "flower", "candle", "grape"]   # List of items
selected_item = random.choice(items)  # Randomly select an item from the list   
guess = input("Guess which item was selected: ")  # Take the user's guess
if guess == selected_item:  # Check if the guess is correct
    print("Congratulations! {selected_item} is correct!")  # Print a message for a correct guess
else:   
    print(f"Sorry, the selected item was {selected_item}. YOU LOST!") 
