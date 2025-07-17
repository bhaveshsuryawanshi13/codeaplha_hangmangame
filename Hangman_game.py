import random
# Word list
words = ['apple', 'robot', 'plane', 'chair', 'spoon']
word = random.choice(words)  # Pick a random word
guessed = ""  # Store all guessed letters
tries = 6  # Max wrong guesses
# Game loop
while tries > 0:
    blanks = ""
    for letter in word:
        if letter in guessed:
            blanks += letter
        else:
            blanks += "_"
    print("Word:", blanks)
    if blanks == word:
        print("🎉 You guessed it right! The word was", word)
        break
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("You already guessed that.")
        continue
    guessed += guess
    if guess not in word:
        tries -= 1
        print("Wrong! Tries left:", tries)
if tries == 0:
    print("❌ Game Over! The word was", word)