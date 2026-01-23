print("----Text Adventure Game----")
print("1) Left")
print("2) Right")
print("3) Forward")
print("Only use numbers to select your option")

while True:
    choice = input("Choose a direction: ")
    if choice == "2":
        print("You have made it to the hallway")
        break
    elif choice == "1" or choice == "3":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")

while True:
    print("1) Left")
    print("2) Right")
    print("3) Forward")
    choice = input("Choose a direction: ")
    if choice == "3":
        print("You have made it to the kitchen. There is 3 entrances")
        break
    elif choice == "1" or choice == "2":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")

while True:
    print("1) Left")
    print("2) Right")
    print("3) Forward")
    choice = input("Choose a direction: ")
    if choice == "2":
        print("You have made it to spooky room with dolls.")
        break
    elif choice == "1" or choice == "3":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")

while True:
    print("1) Left")
    print("2) Right")
    print("3) Forward")
    choice = input("Choose a direction: ")
    if choice == "1":
        print("You have made it through. You sense that your close to the exit")
        break
    elif choice == "3" or choice == "2":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")

while True:
    print("1) Left")
    print("2) Right")
    print("3) Forward")
    choice = input("Choose a direction: ")
    if choice == "2":
        print("You have made it through. You see the exit infront of you")
        break
    elif choice == "3" or choice == "1":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")

while True:
    print("1) Left")
    print("2) Right")
    print("3) Forward")
    choice = input("Choose a direction: ")
    if choice == "3":
        print("CONGRATS! YOU WON!")
        break
    elif choice == "2" or choice == "1":
        print("Wrong way.")
    else:
        print("Please enter 1, 2 or 3")
    


