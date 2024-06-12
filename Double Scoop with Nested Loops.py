# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

import random  # Import the random module
moods = ["happy", "sad", "energetic", "calm", "angry", "excited", "tired"]      # List of moods  
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # List of days
times = ["morning", "afternoon", "evening"]  # List of times of the day
for day in days:  # Loop through the days of the week
    for time in times:  # Loop through the times of the day
        mood = random.choice(moods)  # Randomly select a mood from the list
        print(f"On {day}, in the {time}, you were feeling {mood}")  # Print the day, time, and mood