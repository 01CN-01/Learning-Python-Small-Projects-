def int_checker(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number.")

def input_checker(prompt):
    while True:
        answer = input(prompt)
        if answer != "":
            return answer
        else:
            print("Cannot leave blank.")

def round_number(prompt):
    while True:
        try:
            answer = float(input(prompt))
            return round(answer, 2)
        except ValueError:
            print("Enter a Number.")