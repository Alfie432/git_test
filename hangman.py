import random as r

words = ["cool", "metal", "command", "width", "first", "python", "javascript"]
letter_list = []
word = r.choice(words)
for letter in word:
    letter_list.append(letter)
lives = 6


# For checking game loop uncomment the print statement
# print(word)

while True:
    # Conditionals to check for before asking a user

    # What to do if you have no remaining lives left
    if lives == 0:
        print("You ran out of lives :(")
        print(f"The word was {word}")
        break

    # What to do if user guessed the word
    if len(letter_list) == 0:
        print(f"You Guessed the word {word}! You win!")
        break

    # What to if user makes it through all the conditionals

    # Ask for guess
    guess = str(input("Please Guess a Letter: "))

    if len(guess) == 1:

        # What to do with guess
        if guess in word:
            print("Correct!")
            letter_list.remove(guess)
        else:
            print("Incorrect. Try again")
            lives -= 1

    else:
        print("Guess must be only one character long")
