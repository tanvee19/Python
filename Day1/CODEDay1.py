# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:45:05 2019

@author: Tanvee
"""

'''Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""
'''
print("Gas Mileage Calculator")
kilometers = int(input("enter the kimlometers travelled by the car"))
litres = int(input("enter the liters of fuel in the car"))
avg = kilometers/litres
print(avg)


"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
""" 

print("Ride host calculator")
travel = int(input("enter the distance travelled in a day "))
cod=80
vfavg = int(input("vehicle fuel average "))
l= travel / vfavg
l= 80*l
print(l)

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

print("Weighted Score Calculator")
ass=input("enter the marks of 3 assignment")
print(ass.split())
exam=input("enter the marks of 2 exams")
print(exam.split())
wSc = (float(ass[0]+ass[1]+ass[2])*0.1)+(float(exam[0]+exam[1])*0.35)
print(wSc)


"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *

"""

print("Name Printing Checkerboard pattern")
i=0
while i<7:
    if(i in [0,2,4,6]):
        print("* "*8)
    else:
        print(" "+"* "*8)
    i=i+1



"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

import math
#dir(math)
#help(math.factorial)
print("Factorial")
Fact = int(input("enter the number "))
print(math.factorial(Fact))


"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

print("Styling of String")
#dir(str)
#help(str.title)
str1= input("Enter the string ")
print(str1.lower())
print(str1.upper())
print(str1.title())

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

print("    Replacing of Characters    ")
str1= "RESTART"
a=str1.find('R')
#print(a)
b=str1[:a+1]
c=str1[a+1:]
print(b+c.replace('R','$'))



"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

print(" String Handling")
s=input("enter the name").split()
print(s[1]+' '+s[0])



#help(str.index)

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

print(" Formatted String ")
a = input("enter the input ")
print(a.replace(' ','*'))


"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

i=1
while i<=100:
    if((i%15)==0):
        print("fizzbuzz")
    else:
        if((i%5)==0 and (i%3)!=0):
            print("buzz")
        if((i%3)==0 and (i%5)!=0 ):
            print("fizz")
        else:
            print(i)
    i=i+1
    
    







































