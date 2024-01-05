#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer != "Friday": 
    round += 1     # increase the round counter by 1
    answer = input('What is the best day of the week?: ')
    if answer == "Friday": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet been reached
        print("Sorry, the answer was Friday.")
    else:                  # if answer was wrong
        print("Sorry. Try again!")

