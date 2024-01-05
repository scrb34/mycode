#!/usr/bin/env python3
"""Linux command line game! User has 5 questions to answer to show their command line mastery!"""

print("Welcome to my Linux Command Line quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's play!")
score = 0

answer = input("What does mkdir stand for? ")
if answer.lower() == "make directory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was make directory")

answer = input("What does cd stand for? ")
if answer.lower() == "change directory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was change directory!")

answer = input("What does rm stand for? ")
if answer.lower() == "remove":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was remove!")

answer = input("What does rmdir stand for? ")
if answer.lower() == "remove directory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer was remove directory")

answer = input("Would you like to try a bonus question? ")
if answer.lower() == "yes":
    print('Great!! Let\'s go!')
else:
    print("You got " + str(score) + " questions correct!")
    print("Thanks for playing!")
    quit()

answer = input("What does su stand for? ")
if answer.lower() == "switch user":
    print('Correct!')
    score += 1
else:
    print("Sorry that was incorrect! The correct answer was switch user ")

print("Thanks for playing!")
print("You got " + str(score) + " questions correct!")



