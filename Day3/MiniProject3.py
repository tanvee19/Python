# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:18:28 2019

@author: Tanvee
"""

# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""

print("Hangman Letter")
import random
list1 = ['Apple','Mango','Banana','Papaya','Watermelon','Grape','Orange','Mosami','Berry']
value = random.choice(list1)
input1 = input("Enter the gussed value :  ")
f=0
for i in value:
    for j in input1:
        if i == j:
            f=1
            pass
        else:
            f=0
            exit
if f==1:
    print("player wins and computer lose.")
else:
    print("player lose and computer wins.")
"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

print("Hangman Letter")
import random
def randomno():
    list1 = ['Apple','Mango','Banana','Papaya','Watermelon','Grape','Orange','Mosami','Berry']
    return random.choice(list1)
def guess(value):
    input1 = input("Enter the gussed value :  ")
    f=0
    for i in value:
        for j in input1:
            if i == j:
                f=1
                pass
            else:
                f=0
                exit
    if f==1:
        print("player wins and computer lose.")
    else:
        print("player lose and computer wins.")
        
value = randomno()
guess(value)
    
    
"""
Challenge 3
Read the words from a file

"""
f = open('text.txt',"r")
lines = f.readlines()
for i in lines:
    values = i.split(" ")
    for i in values:
        guess(i)

def guess(value):
    input1 = input("Enter the gussed value :  ")
    f=0
    for i in value:
        for j in input1:
            if i == j:
                f=1
                pass
            else:
                f=0
                exit
    if f==1:
        print("player wins and computer lose.")
        print("value : "+ value)
    else:
        print("player lose and computer wins.")


"""
Challenge 4
    Get the list of Internet after web scrapping
"""






























