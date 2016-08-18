#!/usr/bin/python3

#Magic8Ball Project
#r/beginnerprojects http://bit.ly/29SecUw
#Only did 8 responses because it's an 8 ball.
#No GUI yet. 

import random
import time
import sys
getAnswer = ['It is certain.', 'Hmmm, not sure. Ask again later.', 'No.', 'Doubtful.', 'Outlook does not look so good.', 'Yes.', 'Is that what you really want to ask?', 'It is decidedly so.']

def printAnswer():
    input("Ask your question: ")
    print("\nThinking....\n")
    time.sleep(3)
    print(random.choice(getAnswer))
    print(' ')
    again()

def again():
    newQ = input("Would you like to ask another question? ").lower()
    if newQ == 'yes' or newQ == 'yeah' or newQ == 'y':
        printAnswer()
    else:
        print("Ok, bye bye.")
        sys.exit()

print("I am the Magic 8 Ball!")
printAnswer()
    

