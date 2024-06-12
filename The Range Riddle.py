# Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

import random  # Import the random module
moods = ["happy", "sad", "energetic", "calm", "angry", "excited", "tired"]      # List of moods  # List of moods
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # List of days   
for i in range(len(days)):  # Loop through the days of the week
    day = days[i]  # Get the day from the list
    mood = random.choice(moods)  # Randomly select a mood from the list
    print(f"On {day}, you were feeling {mood}")  # Print the day and the mood


