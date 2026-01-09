secret_word = "python"
index = 0
while True:
    user_input = input(f"Let's guess the secret word letter by letter!\n Masukkan huruf ke {index + 1}: ").lower()
    if len(user_input) == 1 and user_input[0] == secret_word[index]:
        print(f"Correct! The letter is '{secret_word[index]}'.")
        index += 1  
    else:
        print("Incorrect, try again!")
    if index == len(secret_word):
        print(f"Congratulations! You've guessed the secret word '{secret_word}' correctly!")
        break