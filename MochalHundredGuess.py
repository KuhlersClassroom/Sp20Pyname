import random

Number = "nil"
PlayerNumber = 0
InputNumber = 0
Count = 0

Number = random.randrange(101)
print("The number", Number, "was randomly generated.")

while max([Count]) < 8:
    PlayerNumber = None
    while PlayerNumber is None:
        InputNumber = input("Pick a number from 1 to 100. ")
        InputNumber = int(InputNumber)
        if InputNumber > 0 and InputNumber < 100:
            PlayerNumber = InputNumber
        else:
            print("Please pick a valid number from 1 to 100.")
    Count += 1
    
    if PlayerNumber == Number:
        if Count == 1:
            print("You guessed it after", Count, "guess.")
        else:
            print("You guessed it after", Count, "guesses.")
        Count = 8
    elif PlayerNumber > Number:
        print("Lower")
    else:
        print("Higher")
