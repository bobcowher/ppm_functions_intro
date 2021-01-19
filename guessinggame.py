import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("You entered a non-numeric number")
            print("")


highest = 1000
lowest = 1

answer = random.randint(lowest, highest)


while(True):


    print("Please guess a number between {0} and {1}: ".format(lowest, highest))
    guess = int(get_integer(": "))
    if guess < answer:
        if guess == 0:
            print("Terminating program")
            print("The correct answer would have been {}".format(answer))
            exit(0)
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("You got it!")
        exit(0)