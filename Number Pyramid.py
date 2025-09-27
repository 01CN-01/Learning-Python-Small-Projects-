pyramid = input("How long do you want the pyramid to be: ")
pyramid = int(pyramid)
text = input("What would you pyramid look like? ")

for i in range(1, pyramid + 1):
    print(text * i)