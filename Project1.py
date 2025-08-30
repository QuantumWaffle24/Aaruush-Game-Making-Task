import random

print("--Random Number Guessing Game--")

lowestnumber = 1
highestnumber = 100
randomnumber = random.randint(lowestnumber,highestnumber)
attempts = 0
print(f"Select A Number Between {lowestnumber} And {highestnumber}")

while True:
    guess = input("Enter Your Guess:")
    if not guess.isdigit():
        print(f"Invalid Input! Please Select A Number Between {lowestnumber} and {highestnumber}")
        continue
    guess = int(guess)
    attempts += 1
    if randomnumber > guess: 
        print("Guess Higher")
    elif randomnumber < guess:
        print("Guess Lower")
    else:
        print("BINGO!")
        print(f"Number Of Guesses:{attempts}")
        break
    


