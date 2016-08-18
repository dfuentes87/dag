#!/usr/bin/python3

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
        else:
            break
while True:
    try:
        number = int(input("Enter an integer: "))
        collatz(number)
        break
    except ValueError:
        pass
    print("Not valid! Please enter an integer: ")
