import random

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "html"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        if display_word == secret_word:
            print("Congratulations! You guessed the word!")
            break
        
        if attempts == 0:
            print(f"Out of attempts! The word was {secret_word}.")
            break
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in secret_word:
                attempts -= 1

if __name__ == "__main__":
    hangman()
