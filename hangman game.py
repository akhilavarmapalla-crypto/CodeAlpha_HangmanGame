import random

def play_hangman():
    words = ["python", "hangman", "computer", "keyboard", "program"]
    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {max_wrong_guesses} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong_guesses:
        # Display current progress
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display)

        # Check win condition
        if "_" not in display:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            remaining = max_wrong_guesses - wrong_guesses
            print(f"Wrong guess! You have {remaining} incorrect guesses left.")

        print("Guessed letters so far:", ", ".join(guessed_letters))
        print("-" * 40)

    if wrong_guesses == max_wrong_guesses:
        print("\nGame Over! You've used all your incorrect guesses.")
        print("The word was:", word)


if __name__ == "__main__":
    play_hangman()
