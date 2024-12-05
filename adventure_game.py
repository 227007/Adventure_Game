import time
import random

def delayed_print(message, delay=1):
    """Prints a message with a delay."""
    print(message)
    time.sleep(delay)

def show_intro():
    """Displays the introduction to the game."""
    delayed_print("Welcome to the Adventure Game!")
    delayed_print("You can explore, rest, or exit the game.")
    delayed_print("Make your choice wisely!")

def get_valid_choice():
    """Prompts the player for a valid choice."""
    while True:
        choice = input("What would you like to do? (explore/rest/exit): ").lower()
        if choice in ['explore', 'rest', 'exit']:
            return choice
        delayed_print("Invalid choice. Please choose 'explore', 'rest', or 'exit'.")

def handle_exploration():
    """Handles the exploration logic and returns the result."""
    delayed_print("You venture into the unknown...")
    # Randomly determine if the player wins or loses
    outcome = random.choice(['win', 'lose'])
    if outcome == 'win':
        delayed_print("You found treasure and won the game!")
        return True
    else:
        delayed_print("You encountered a monster and lost the game!")
        return False

def take_rest():
    """Simulates resting in the game."""
    delayed_print("You take a moment to rest and regain your strength.")

def game_loop():
    """Main loop that controls the game's flow."""
    show_intro()
    
    while True:
        player_choice = get_valid_choice()
        
        if player_choice == 'explore':
            game_result = handle_exploration()
            if game_result is not None:
                if game_result:
                    delayed_print("You win! Would you like to play again? (yes/no)", 2)
                else:
                    delayed_print("You lost! Would you like to try again? (yes/no)", 2)
                
                while True:  # Loop to ensure valid input for restarting
                    restart_choice = input().lower()
                    if restart_choice in ['yes', 'no']:
                        break
                    delayed_print("Please answer with 'yes' or 'no'.", 2)
                
                if restart_choice != 'yes':
                    delayed_print("Thanks for playing! Goodbye!", 2)
                    break
        
        elif player_choice == 'rest':
            take_rest()
        
        elif player_choice == 'exit':
            delayed_print("Thanks for playing! Goodbye!", 2)
            break

if __name__ == "__main__":
    game_loop()
