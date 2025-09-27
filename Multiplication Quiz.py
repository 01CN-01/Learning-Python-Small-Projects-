print("-------This is a multiplication quiz-------")
questions = input("How many questions would you want in the quiz: ")
questions = int(questions)

score = 0

for i in range(1, questions+1):
        answer = input(f"Question {i}: What is {i} x {i + 2}? ")
        if int(answer) == i * (i + 2):
            score += 1
            print("Correct! Your score = ",score ,"/", i)
        else:
            print("Incorrect! Your score = ",score ,"/", i )
    

