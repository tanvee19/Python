# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:16:01 2019

@author: Tanvee
"""

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""
import random
a = int(input(" enter the number   "))
b=random.randint(0,100)
if(a==b):
    print("Player wins")
else:
    print("player loses")
    
    
"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""
import random
a = int(input(" enter the number   "))
b=random.randint(0,100)
if(a==b):
    print("Player wins")
else:
    print("player loses! the number is {}".format(b))
    
    
"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""
import random
a = int(input(" enter the number   "))
b=random.randint(0,100)
if(a<b):
    print("too low")
else:
    print("too high")
    
    




"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""

import random
b=random.randint(0,100)
while a!=b:
    a = int(input(" enter the number   "))
    if(a==b):
        print("Player wins")
        break;
    else:
        print("player loses!")
    
"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""

import random
b=random.randint(0,100)
i=0
while i<6:
    a = int(input(" enter the number   "))
    if(a==b):
        print("Player wins")
        break;
    else:
        print("player loses!")
    i=i+1
        
        
"""
Challenge 6
    Print the number of tries left 
"""

import random
b=random.randint(0,100)
i=0
while i<6:
    a = int(input(" enter the number   "))
    if(a==b):
        print("Player wins")
        break;
    else:
        print("player loses!")
    print("No. of tries left" + str(6-i-1))
    i=i+1
        
    
    
"""
Challenge 7
    Lets give user the option to play again
"""

import random
t=True
while(t):
    b=random.randint(0,100)
    i=0
    while i<6:
        a = int(input(" enter the number   "))
        if(a==b):
            print("Player wins")
            break;
        else:
                print("player loses!")
        print("No. of tries left" + str(6-i-1))
        i=i+1
    s=input("Wanna Play Again : Type Y  ")
    if s=='Y' or s=='y':
        t=True
    else:
        t=False
        
        
        
        
        
"""
Challenge 8
    Catch when someone submits a non integer
"""    
import random
help()
b=random.randint(0,100)
i=0
while i<3:
    try:
        a = int(input(" enter the number   "))
    except ValueError:
        print("enter valid no.")
        break;
    if(a==b):
        print("Player wins")
        break;
    else:
        print("player loses!")
    print("No. of tries left" + str(3-i-1))
    i=i+1


    
    
    