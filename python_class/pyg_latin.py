#!/usr/bin/python3

#Taking the Code Academy PygLatin lesson and adding improvements. 

pyg = "ay"

print('This is the PygLatin Translator!')

#Added a while loop to keep asking for a word if none is entered.
original = input("Enter a word to translate: ")
while len(original) == 0 or not original.isalpha():
    original = input("Please enter a valid word to translate: ")

word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
print(new_word) 
    
