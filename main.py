import art
import random

print(art.logo)

play = True
while play:
    print("Welcome to the guessing number game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Pick a difficulty. Type 'easy' or 'hard'.\nType 'exit' to stop.\n").lower()

    if difficulty == "exit":
        play = False
        continue

    chances = 5
    if difficulty == "easy":
        chances = 10

    number = random.randint(1, 100)
    guessed = False
    while chances > 0 and not guessed:
        chances -= 1
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You did it! The answer was {number}")
            guessed = True
        else:
            if guess < number:
                print(f"Too low.")
            else:
                print(f"Too high.")
            print(f"You have {chances} attempts remaining to guess the number.")

