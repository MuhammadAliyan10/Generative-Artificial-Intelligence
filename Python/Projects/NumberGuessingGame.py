import random

randomNumber : int = random.randint(0,100)
guess : int = 0

while True:
    userGuess : int = int(input("Enter a number between 0 to 100 : "))
    if userGuess == randomNumber:
        guess += 1
        print(f"You won the game in {guess} guess.")
        break
    print("You number is less then guess number") if userGuess <  randomNumber else print("Your number is greater then guess number.")
    guess = guess + 1
