import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

while True:
    # Wait for the user to press Enter to roll the dice
    input("Press Enter to roll the dice...")
    
    # Print the result of the dice roll
    print("You rolled a", roll_dice())
    
    # Ask if the user wants to roll again; break the loop if the answer is not 'y'
    if input("Roll again? (y/n): ").lower() != 'y':
        break