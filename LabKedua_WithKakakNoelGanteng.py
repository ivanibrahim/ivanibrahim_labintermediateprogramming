secret_word = "python"
display_word = ['_'] * len(secret_word)
user_guessed_letters = []
max_attempt = 6
while True:
    if "_" not in display_word:
        print(f"Congratulations! You've guessed the secret word '{secret_word}' correctly!")
        break
    elif max_attempt == 0:
        print(f"Sorry, you've run out of attempts! The secret word was '{secret_word}'.")
        break
    else:
        user_input = input(f"Let's guess the secret word letter by letter! ").lower()
        if len(user_input) == 1 and user_input in secret_word and user_input[0] not in user_guessed_letters:
            user_guessed_letters.append(user_input[0])
            max_attempt -= 1
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    display_word[i] = user_input
                    print(f"Guessed Letter: {' '.join(display_word)}")
            print(f"Attempt left : {max_attempt}")
        elif user_input in secret_word:
            print(f"You've already guessed the letter '{user_input[0]}'. Try a different letter.")
        else:
            max_attempt -= 1
            print(f"Incorrect, try again! You have {max_attempt} attempts left.")