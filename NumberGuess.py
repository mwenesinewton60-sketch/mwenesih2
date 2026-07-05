import random

number_to_guess = random.randint(1, 100)
attempts=0
print("Hey nigga, Im somehow thinking of anumber between 1 and 100.")
while True:
    guess = int(input("Enter any number you think of:"))
    attempts += 1

    if guess< number_to_guess:
        print("Does not exist!Try again")
    elif guess > number_to_guess:
        print("Too high! Try again")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
