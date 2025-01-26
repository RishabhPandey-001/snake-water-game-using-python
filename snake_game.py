import random

def game_result(player_choice, computer_choice):
    """Determine the result of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "water" and computer_choice == "gun") or \
         (player_choice == "gun" and computer_choice == "snake"):
        return "Hurray!... You won the Game "
    else:
        return "Ops! You Loose the Game..."

# Main game loop
def play_game():
    print("Welcome to Snake, Water, Gun!")
    print("Choices: snake, water, gun")

    choices = ["snake", "water", "gun"]

    while True:
        # Player's choice
        player_choice = input("\nEnter your choice (or 'quit' to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice not in choices:
            print("Invalid choice! Please choose snake, water, or gun.")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        # Determine the winner
        result = game_result(player_choice, computer_choice)
        print(result)

# Start the game
play_game()

