# Make hangman game function
# Show remaining lives with hearts
def lifes_remaining(max_attempt):
    hearts = '💖 ' * max_attempt
    empty_hearts = '_ ' * (6 - max_attempt)
    return hearts + empty_hearts
#To update the display word with guessed letters
def update_text(display_word):
    display = " "
    for letter in display_word:
        display += letter + " "
    return display
# Main function for the Hangman game
def hangman(secret_word = "python"):
    max_attempt = 6
    display_word = ['_'] * len(secret_word)
    user_guessed_letters = []
    while True:
        #Check if the user has won or lost or still playing
        if "_" not in display_word:
            print(f"Congratulations! You've guessed the secret word '{secret_word}' correctly!")
            break
        elif max_attempt == 0:
            print(f"Sorry, you've run out of attempts! The secret word was '{secret_word}'.")
            break
        else:
            user_input = input(f"Let's guess the secret word: ").lower()
            # If the guessed letter is correct and not guessed before
            if len(user_input) == 1 and user_input in secret_word and user_input[0] not in user_guessed_letters:
                user_guessed_letters.append(user_input[0])
                for i in range(len(secret_word)):
                    if secret_word[i] == user_input:
                        display_word[i] = user_input
                print(f"Correct! The letter is '{user_input[0]}'.")
                print(f"Guessed Letter: {update_text(display_word)}")
                print(f"Life Remaining : {lifes_remaining(max_attempt)}")
            # If the letter has already been guessed
            elif user_input in user_guessed_letters:
                print(f"You've already guessed the letter '{user_input[0]}'. Try a different letter.")
            #Lose a life if the guess is incorrect
            else:
                user_guessed_letters.append(user_input[0])
                max_attempt -= 1
                print(f"Oops, the letter '{user_input[0]}' is not in the secret word. Try again!")
                print(f"Life Remaining : {lifes_remaining(max_attempt)}")
print(f'''Welcome to the Hangman Game! \nIn this game, you will try to guess the secret word letter by letter.\nYou have 6 lives represented by hearts (💖).\nEach incorrect guess will cost you a life.\nThe winner of the game will receive 100.000.000 (ZWL) \nLet's begin the game!''')
hangman("gaksusah")
  