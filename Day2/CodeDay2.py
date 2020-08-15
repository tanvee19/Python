# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:57 2019

@author: Tanvee
"""

"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 
l=[]
for i in range(1,21):
    print(i)
    l.append(i)
even=l[1::2]
print(even)
odd = l[::2]
print(odd)

"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False
def Leapyr(a):
    if((a%4)==0):
        if ((a%100)==0):
            return "Not"
        elif ((a%400)==0):
            return "Leap Year"
    return "Leap Year"
a=Leapyr(2020)
print(a)
    

"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year
def days_in_month(m):
    M1 = ['Jan','Mar','May','July','Aug','Oct''Dec']
    M2 = ['Apr','June','Nov','Sept']
    if m in M1:
        return 31
    if m in M2:
        return 30
    else:
        return 29

days_in_month('Jan')

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

print("Vowels Finder")
states = ['Raj','Guj','Mahara','Bengal']
s=''
l=[]
for i in states:
    for j in i:
        if j in ['a','e','i','o','u']:
            pass
        else:
            s=s+j
    l.append(s)
    s=''
print(l)


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

print("Pattern Builder")
x=int(input("Enter the size :"))
for i in range(1,x+1):
    print("* "*i)
for i in range(x-1,0,-1):
    print("* "*i)


"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

print("Pallindromic Integer")
user_input = input("Enter space seperated values :").split()

input_length  = len(user_input)
count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True

print(pallindromic_integer)


# Short Logic using the all and any keyword

# give list of inputs from user
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    




"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

print("Pangram")
def Pangram(a):
    str1 = a.lower()
    list1 = []
    for char in str1:
        if char not in list1:
            if char in  "abcdefghijklmnopqrstuvwxyz":
                list1.append(char)
    if len(list1) == 26:
        return "P"
    else:
        return "NP"
a=Pangram("The quick jumps over the lazy dog")
print(a)


"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
print("Bricks")
def make_bricks(small, big, goal):
    if goal % 5 > small:
        print (False) 
    else:    
        c = big*5 + small
        if c >= goal:
            print (True)
        else:
            print (False)

lst = input("Enter Numbers: ").split(",")

my_list=[]

for i in lst:
    my_list.append(int(i))
    
make_bricks(my_list[0], my_list[1], my_list[2])

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
print("Reverse Function")
s="siht si tahw"
print(s[::-1])
"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

print("Translate Function")
def translate(a):
    s=''
    for i in a:
        for j in range(len(a)):
            if i not in ['i','o','e','a','u']:
                s=s+a[j]+'o'+a[j]
    print(s)
    
translate("This is fun")

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

print("Operations Function")
x=input("enter")
x=x.split()
def sum1(x):
    s=0
    for i in x:
        i=int(i)
        s=s+i
    print(s)
def mul(x):
    s=1
    for i in x:
        i=int(i)
        s=s*i
    print(s)
mul(x)
def lar(x):
    l=0
    for i in x:
        i=int(i)
        if l < i:
            l=i
    print(l)
lar(x)
def sm(x):
    l=100000
    for i in x:
        i=int(i)
        if l > i:
            l=i
    print(l)
sm(x)
def sorty(x):
    for i in range(len(x)):
        i=int(i)
        for j in range(0,len(x)):
            if x[i]< x[j]:
                x[i],x[j]=x[j],x[i]
    print(x)
sorty(x)
def dup(x):
    l=[]
    for i in x:
        if i not in l:
            l.append(i)
    print(l)
dup(x)
"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""

print("Sorting")
student_list = []

while True:
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

print("Centered Average")
list1=[1, 2, 3, 4, 100]
summ=0
if len(list1)>2:
    m=max(list1)
    print(m)
    list1.remove(m)
    n=min(list1)
    print(n)
    list1.remove(n)
    for i in list1:
        summ=summ+i
    summ=int(summ/len(list1))
    print(summ)
    
"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

print("Unlucky 13")
summ=0
l2=[]
list1=[13, 1, 2, 13, 2, 1, 13]
if len(list1)>0:
    for i in range(len(list1)):
        if list1[i] not in l2:
            l2.append(list1[i])
            if list1[i] is not 13:
                summ=summ+i
            else:
                i+=1
    print(summ)
else:
    print("0")
