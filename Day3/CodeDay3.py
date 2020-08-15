# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:07:44 2019

@author: Tanvee
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

print("Generator")
value = input("Enter > ")
value = value.split(',')
print(value)
print(tuple(value))
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

print("Weeks")
value = input("Enter the week days > ")
value = value.split(',')
tu1 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for item in tu1:
    if item not in value:
        value.append(item)
print(tuple(value))


"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

print("Supermarket")
dict1 = {'BANANA FRIES' : 12,
    'POTATO CHIPS' : 30,
    'APPLE JUICE' :10,
    'CANDY' :5,
    'APPLE JUICE' :10,
    'CANDY1' : 5,
    'CANDY2' :5,
    'CANDY3' : 5,
    'POTATO CHIPS' :30}

dict1 = dict()
while True:
    uinput = input("Enter > ")
    if not uinput:
        break
    uinput = uinput.split()
    last= len(uinput)-1
    if(uinput[0] not in dict1.keys()):
        dict1[uinput[0]] = int(uinput[last])
    else:
        v= dict1[uinput[0]]
        dict1[uinput[0]] = v+int(uinput[last])
print(dict1)
    

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

def fun(i):
    if i==15 or i==16:
        return i
    elif i in range(13,20):
        return 0
    else:
        return i
print("Teen calculator ")
dict1 = {}
sum1=0
while True:
    input1 = input("> ")
    if not input1:
        #print(summ)
        break
    input1 = input1.split()
    dict1[input1[0]]=int(input1[1])
for i in dict1.values():
    sum1+=fun(i)
print(sum1)





"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

print(" Character Frequency")
input1 = input("Enter > ")
dict1={}
c=0
for item in input1:
    if item not in dict1:
        dict1[item]=1
    else:
        dict1[item]=dict1[item]+1
print(dict1)


"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

co=0
cw=0
input1 = input("Enter string : ")
for i in input1:
    if(i.isalpha()):
        co+=1
    elif(i.isdigit()):
        cw+=1
print(co,cw)
        

"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""

t = input(" > ")
y = input(" > ")    
c=0
if len(t)==len(y):
    for i in t:
        for j in y:
            if i == j:
                c=1
                pass
            else:
                exit
if(c==1):
    print("Anagram")
else:
    print("Not")

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""
l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
l3=[]
for item1 in l1:
    for item2 in l2:
        if(item1==item2):
            l3.append(item1)
print(l3)


"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

print("Duplicate")
list1 = [12,24,35,24,88,120,155,88,120,155]
set(list1)


"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
l  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      
"""

print("Mailing")
old_list = ["janusfury@aol.com",
"ajlitt@me.com",
"dburrows@me.com",
"robles@yahoo.com",
"jshirley@gmail.com",
"saridder@live.com",
"dmiller@mac.com",
"agapow@yahoo.ca",
"hamilton@sbcglobal.net",
"madler@att.net",
"grady@gmail.com",
"iami@gmail.com",
"heroine@gmail.com",
"loxy@att.net",
"violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]

new_list = ["violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]

old_list = set(old_list)
new_list = set(new_list)
old_list = old_list.difference(new_list)
print(list(old_list))