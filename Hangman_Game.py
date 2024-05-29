import random

print("     ===== hp369 =====    ")
print("---------------------------")
print("Welcome to The Hangman Game")
print("---------------------------")

words = ["OCEAN", "MOUNTAIN", "TECHNOLOGY", "INNOVATION", "CULTURE", "EDUCATION", "FREEDOM", "SUSTAINABILITY", "ADVENTURE", "CREATIVITY"]
word = random.choice(words)

total_changes = len(word)
guess_word = "-" * len(word)

print(guess_word)
while total_changes != 0:
    letter = input("Guess a letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guess_word = guess_word[:index] + letter + guess_word[index+1:]
         
        print(guess_word)        

        if guess_word == word:
            print("=================================")
            print("Congratulations 👏 You Won!! 💐 🎉 ")
            print("Word is=>",word)
            break

    else:
        total_changes -= 1
        print("=================")
        print("Incorrect Guess!!")
        print("Remaining changes are=>",total_changes)
        print("======================================")

else:
    print("==========")
    print("Game over,You Lose!!")
    print("============")
    print("Guess word is=>",word)