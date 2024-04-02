import random

# Function to choose a random word from a list of words
def choose_word():
    words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'watermelon']
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Function to provide hints
def provide_hint(word):
    hints = {
        'apple': ["It's a popular fruit.", "It's red or green in color.", "It grows on trees."],
        'banana': ["It's a tropical fruit.", "It's yellow in color.", "It's often used in smoothies."],
        'orange': ["It's citrus fruit.", "It's orange in color.", "It's rich in Vitamin C."],
        'strawberry': ["It's a small, red fruit.", "It's often used in desserts.", "It has seeds on the outside."],
        'grape': ["It grows in bunches.", "It's used to make wine.", "It comes in green, red, and purple varieties."],
        'watermelon': ["It's a large fruit with green skin.", "It's juicy and refreshing.", "It's often eaten in the summer."]
    }
    return random.choice(hints[word])

# Main function for the game
def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Hint:", provide_hint(word_to_guess))

    while True:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")

        if '_' not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("\nYou've run out of attempts! The word was:", word_to_guess)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing!")

# Start the game
hangman()
