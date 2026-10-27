"""
CodeAlpha Python Programming Internship
Task 1: Hangman Game
Author: Intern
Description: A simple text-based Hangman game where the player guesses
             a hidden word one letter at a time within 6 incorrect attempts.
"""

import random
import sys

# Ensure clean UTF-8 output if supported
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Predefined list of words as per simplified scope (at least 5 words)
WORD_LIST = [
    "PYTHON",
    "DEVELOPER",
    "HANGMAN",
    "CODEALPHA",
    "PROGRAMMING"
]

# Visual ASCII stages representing the hangman for 0 to 6 incorrect guesses
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

MAX_INCORRECT_GUESSES = 6


def get_random_word(words: list) -> str:
    """Selects and returns a random uppercase word from the given list."""
    return random.choice(words).upper()


def display_board(hangman_pics: list, incorrect_guesses: list, correct_guesses: list, secret_word: str):
    """Prints the current hangman art, guessed letters, and masked word."""
    # Print the current stage art
    print(hangman_pics[len(incorrect_guesses)])
    
    # Display missed / incorrect guesses
    print("Incorrect guesses (" + str(len(incorrect_guesses)) + "/" + str(MAX_INCORRECT_GUESSES) + "): ", end="")
    if incorrect_guesses:
        print(", ".join(sorted(incorrect_guesses)))
    else:
        print("None")
    
    # Build masked word: reveal guessed letters, show underscore for hidden
    displayed_word = []
    for letter in secret_word:
        if letter in correct_guesses:
            displayed_word.append(letter)
        else:
            displayed_word.append("_")
    
    print("\nWord: " + " ".join(displayed_word))
    print("-" * 40)


def get_player_guess(already_guessed: set) -> str:
    """Prompts the player for a single valid alphabetic character."""
    while True:
        guess = input("Enter a letter: ").strip().upper()
        if len(guess) != 1:
            print("(!) Please enter a single letter.")
        elif not (guess.isalpha() and guess.isascii()):
            print("(!) Invalid input. Please enter an English alphabet letter.")
        elif guess in already_guessed:
            print(f"(!) You have already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Runs a single round of the Hangman game."""
    secret_word = get_random_word(WORD_LIST)
    correct_guesses = set()
    incorrect_guesses = []
    already_guessed = set()

    print("\n" + "=" * 45)
    print("      WELCOME TO CODEALPHA HANGMAN GAME      ")
    print("=" * 45)
    print(f"I have picked a secret word with {len(secret_word)} letters.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect attempts before game over.\n")

    while len(incorrect_guesses) < MAX_INCORRECT_GUESSES:
        display_board(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)
        
        # Check if user has guessed all unique letters in the secret word
        if set(secret_word).issubset(correct_guesses):
            print("\n" + "=" * 40)
            print("   *** CONGRATULATIONS! YOU WON! ***   ")
            print("=" * 40)
            print(f"You successfully guessed the word: {secret_word}")
            return True

        guess = get_player_guess(already_guessed)
        already_guessed.add(guess)

        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"\n[+] Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            remaining = MAX_INCORRECT_GUESSES - len(incorrect_guesses)
            print(f"\n[-] Sorry, '{guess}' is NOT in the word. (Remaining attempts: {remaining})")

    # If loop ended, player ran out of attempts
    display_board(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)
    print("\n" + "=" * 40)
    print("   *** GAME OVER! YOU RAN OUT OF ATTEMPTS ***   ")
    print("=" * 40)
    print(f"The secret word was: {secret_word}")
    return False


def main():
    """Main function controlling game loop and replay."""
    try:
        while True:
            play_game()
            print("\n" + "-" * 40)
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("\nThank you for playing CodeAlpha Hangman! Goodbye!\n")
                break
    except (KeyboardInterrupt, EOFError):
        # Exit cleanly if the user closes the terminal or presses Ctrl+C.
        print("\n\nGame interrupted. Thank you for playing CodeAlpha Hangman!\n")


if __name__ == "__main__":
    main()
