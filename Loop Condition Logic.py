# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.

# Infinite loop with break statement    
candy = 1  # Initialize the count variable
while candy > 0:  # Infinite loop   
    print("There's more candy")  # Print a statement
    candy = candy + 1  # Increment the count variable
    if candy == 6: 
        break  # Exit the loop

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met.
# Infinite loop with a condition that will eventually be true  
# 
candy = 10   # Initialize the count variable
while candy > 0:  # Infinite loop   
        print("There's more candy")  # Print a statement
        candy = candy - 1  # Decrement the count variable
else:
    print("No more candy")  # Print a statement



        




