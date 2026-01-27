def input_checker(prompt):
    answer = input(prompt)
    if answer != "":
        return answer
    else:
        print("Cannot leave empty.")


def int_checker(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number.")
            