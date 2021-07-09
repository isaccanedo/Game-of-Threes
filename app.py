import random

def add_or_subtract(number):
    if (((number + 1) % 3) == 0):
        print(int(number), ' 1')
        number += 1
    elif (((number - 1) % 3) == 0):
        print(int(number), ' -1')
        number -= 1

    return number

def play(number):
    if (number == 1):
        print(int(number))
    elif ((number % 3) == 0):
        print(int(number), ' 0')
        play(number / 3)
    else:
        play(add_or_subtract(number))

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def init():
    while True:
        print('Input a number to start the game!')
        print('> ', end="")

        number = input()

        if (represents_int(number)):
            number = int(number)

            break

    play(number)

init()
