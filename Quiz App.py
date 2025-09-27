
print("This is a Quiz App about me.")
score = 0
valid_answer = ["a", "b", "c", "d"]

#First Question
print("A) 16")
print("B) 18")
print("C) 19")
print("D) 21")
age = input("How old am I?: ").lower()
while True: #Constant Loop until conditions is met (Only a,b,c,d)
    if age in valid_answer: #Converts "age" variable to lower case and checks if it matches with the valid answers
        break
    else:
        age = input("Please put A, B, C or D: ")


if age == "b":
    score += 1
    print("Correct!")
    print("Score: ", score)
else:
    print("Incorrect!")
    print("Score: ", score)

#Second Question
print("A) Dragon Ball Z")
print("B) Blue Exorcist")
print("C) Bleach")
print("D) Naruto")
anime = input("Whats the first ever anime I've watched?: ").lower()

while True:
    if anime in valid_answer:
        break
    else:
        anime = input("Please put A, B, C or D: ")
if anime == "a":
    score += 1
    print("Correct!")
    print("Score: ", score)
else:
    print("Incorrect!")
    print("Score: ", score)

#Third Question
print("A) 2")
print("B) 5")
print("C) 1")
print("D) 8")
siblings = input("How many siblings do I have?: ")

while True:
    if siblings in valid_answer:
        break
    else:
        siblings = input("Please put A, B, C or D: ")
if siblings == "d":
    score += 1
    print("Correct!")
    print("Score: ", score)
else:
    print("Incorrect!")
    print("Score: ", score)

#Finish
print("The quiz is now over")
print("Score: 1 /", score)



