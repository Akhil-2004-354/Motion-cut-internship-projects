# number guessing game
import random

def guess_the_number():
    # Set range for random number
    min_value = 1
    max_value = 100

    # Generate random number
    number_to_guess = random.randint(min_value, max_value)

    # Set maximum attempts
    max_attempts = 6

    print(f"Welcome to Guess the Number Game!")
    print(f"I'm thinking of a number between {min_value} and {max_value}.")
    print(f"You have {max_attempts} attempts.")

    attempts = 0
    while attempts < max_attempts:
        # Get player's guess
        while True:
            try:
                player_guess = int(input(f"Enter your guess (Attempt {attempts+1}/{max_attempts}): "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Validate player input
        if player_guess < min_value or player_guess > max_value:
            print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
            continue

        attempts += 1

        # Check player's guess
        if player_guess < number_to_guess:
            print("Too low!")
        elif player_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    # Player ran out of attempts
    print(f"Sorry, you didn't guess the number. It was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()




