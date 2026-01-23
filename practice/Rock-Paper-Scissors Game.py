import random

def rock_paper_scissors_game():
    try:
        rounds = input("How many round would you like to play? ")
    except ValueError:
        print("Use a number.")

    score = 0

    rounds = int(rounds)
    for i in range(rounds):
        game_choice = "rock", "paper", "scissors" 
        computer = random.choice(game_choice) #Assign variable to random choice

        choice = input("Choose either rock, paper, scissors: ")
        if choice == "rock":
            #Rock winner factor
            if  computer == "rock":
                print("You have tied. Score: ",score," / ",i + 1)
            elif computer == "paper":
                print("You have lost. Score: ",score," / ",i + 1)
            elif computer == "scissors":
                score += 1
                print("You have won. Score:",score," / ",i + 1)
        #------------------------------------
        elif choice == "paper":
            if  computer == "rock":
                score += 1
                print("You have won. Score:",score," / ",i + 1)
            elif computer == "paper":
                print("You have tied. Score: ",score," / ",i + 1)
            elif computer == "scissors":
                print("You have lost. Score: ",score," / ",i + 1)
        #------------------------------------
        elif choice == "scissors":
            #Scissors winner factor
            if  computer == "rock":
                print("You have lost. Score: ",score," / ",i + 1)
            elif computer == "paper":
                score += 1
                print("You have won. Score:",score," / ",i + 1)
            elif computer == "scissors":
                print("You have tied. Score: ",score," / ",i + 1)
        else:
            print("Invalid Option")

score = 0

game_choice = "rock", "paper", "scissors" 
computer = random.choice(game_choice) #Assign variable to random choice

#Starts Game
rock_paper_scissors_game()


try:
    while True:
        exit_program_decision = input("Would you like to keep playing? (Y / N): ").lower()
        if exit_program_decision == "y":
            rock_paper_scissors_game()
        elif exit_program_decision == "n":
            print("Goodbye!")
            break
        else:
            print("Please enter either (Y / N)")
except ValueError:
    print("Invalid Option.")
