from art import logo
import random

# computer choosing random number between 1 and 100
def computer_number():
    number = random.randrange(1, 101)
    return (number)

def comparison(number, guess):
    if number < guess:
        return ("Too High")
    elif number > guess:
        return ("Too Small")
    elif number == guess:
        return ("You got it right!! You WON")

def difficulty(number, easy, hard):
    if easy:
        n = 10
    elif hard:
        n = 5
    while n > 0:
        print(f"You have {n} attempts remaining")
        guess = int(input("Make a Guess:"))
        result = comparison(number, guess)
        print(result)
        if result == "You got it right!! You WON":
            break
        n = n-1
    if n == 0:
        print("You Lose You lost all guesses")


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!!!")
    print("I'm thinking of a number between 1 and 100")
    number = computer_number()
    print(number)
    choice_one = input("Choose a difficulty, Type 'easy' or 'hard':").lower()
    difficulty(number, choice_one == "easy", choice_one == "hard")
main()



