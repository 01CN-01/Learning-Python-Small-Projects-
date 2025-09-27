import random

number = random.randint(1,10)

print("I have a number in my head")

while True:
    guess = int(input("Guess what number I am thinking of?"))
    if guess == number:
        print("YOU GOT IT RIGHT!")
        break
    else:
        print("Unlucky... The number was",number,"Try again!")