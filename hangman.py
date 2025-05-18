import random

def choose_word():
    word_list = ["python", "hangman", "developer", "internship", "project"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    word = choose_word()
    guessed_letters = []
    tries = 6

    print("🎮 Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("✅ Good guess!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f"❌ Wrong guess. Tries left: {tries}")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("🎉 Congratulations! You guessed the word!")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_game()
