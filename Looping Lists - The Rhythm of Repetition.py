# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for i in range(len(genres)):
    print(f"Track {i+1} is a {genres[i]} song!")

# Task 2: The Remix Artist with while
# Rewrite the previous task using a while loop instead of a for loop.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0
while i < len(genres):
    print(f"Enjoy this {genres[i]} song!")
    i += 1
    if genres [i] == "Hip-hop":
        print("No Hip-Hop songs, the party is over!")
        break

# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

index = range(len(genres))
for i in index: 
    if genres[i] == "Classical":
        continue # Skip the Classical genre 
    print(f"Track {i+1} the light show is ready!")




