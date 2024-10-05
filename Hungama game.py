# hungama game
import random

# Word list
words = ['apple', 'banana', 'cherry', 'date', 'strawberry']

def hangman():
    word = random.choice(words)
    word_length = len(word)
    display = ['_'] * word_length
    incorrect_guesses = 6
    guessed_letters = []

    print("Welcome to Hangman Challenge!")

    while incorrect_guesses > 0 and '_' in display:
        print(' '.join(display))
        print(f"Incorrect guesses remaining: {incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess not in word:
            print("Incorrect guess!")
            incorrect_guesses -= 1
            guessed_letters.append(guess)
        else:
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
            guessed_letters.append(guess)

    if '_' not in display:
        print(' '.join(display))
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was {word}.")

if __name__ == '__main__':
    hangman()

