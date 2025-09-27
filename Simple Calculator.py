
def wholething():
    print("----------Calculator----------")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    while True:
        selection = (input("Select out of the options (1 - 4): "))
        if selection in selection_options:
            break
        else:
            print("Select from option 1-4")

    if selection == "1":
        print("You have selected Addition")
        firstnumber = int(input("Firstnumber: "))
        secondnumber = int(input("Secondnumber: "))
        sum = firstnumber + secondnumber
        print(firstnumber,"+",secondnumber, "=", sum)
    if selection == "2":
        print("You have selected Substraction")
        firstnumber = int(input("Firstnumber: "))
        secondnumber = int(input("Secondnumber: "))
        subtraction = firstnumber - secondnumber
        print(firstnumber,"-",secondnumber, "=", subtraction)
    if selection == "3":
        print("You have selected Multiplication")
        firstnumber = int(input("Firstnumber: "))
        secondnumber = int(input("Secondnumber: "))
        multiplication = firstnumber * secondnumber
        print(firstnumber,"*",secondnumber, "=", multiplication)
    if selection == "4":
        print("You have selected Division")
        firstnumber = int(input("Firstnumber: "))
        secondnumber = int(input("Secondnumber: "))
        division = firstnumber / secondnumber
        print(firstnumber,"/",secondnumber, "=", division)

selection_options = ["1", "2", "3", "4"]

wholething()


again = input("Would you like to use the calculator again? (Y/N): ")
if again.lower() == "y":
    wholething()
else:
    print("You have exited out of the program")




