4# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:39:11 2019

@author: Tanvee
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

print("Copy")
with open("text.txt","rt") as fp:
    with open("Copy.txt",'wt') as ft:
        for lines in fp:
            ft.write(lines)
with open("Copy.txt","rt")as ft:
    print(ft.readlines())
        

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
print("Absentees")
i=0
with open("text.txt",'wt')as f:
    while i<25:
        input1 = input("Enter name : ")
        if not input1:
            break
        f.write(input1+'\n')
    
with open("text.txt","rt")as ft:
    print(ft.readlines())
"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
'''
import csv
with open("Zoo.csv") as csv_file:
    summ=0
    L1=[]
    # row has the list of all columns
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if row[0] not in L1:
            L1.append(row[0])
    s = ''
    for i in L1:
        s = s+ i+' / '
    l =  len(s)-1
    print("("+s[:l-1]+')')
 ''' 

           
import csv

animal_groups = {}
water = {}
summ = 0
with open("Zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        if row[0] in animal_groups:
            animal_groups[row[0]] = animal_groups[row[0]] + 1
        else:
            animal_groups[row[0]] = 1
    
with open("Zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)    
    for row in csv_reader:
        if row[0] in water:
            water[row[0]] = int(water[row[0]]) + int(row[2])
        else:
            water[row[0]] = int(row[2])
            
print(animal_groups)
print(water)

        
with open("Zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file)        
    next(csv_reader)
    for row in csv_reader:
        row[2] = int(row[2])
        summ=summ+row[2]
    print(summ)
                

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

dict1 = {}
with open("c.txt",'rt') as f:
    for k in f:
        print(k)
        values = k.split(" ")
        print(values)
        for j in values:
            if j not in dict1:
                dict1[j] = 1
            else:
                dict1[j] = int(dict1[j]) + 1
print(dict1)


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
l=[]
try:
    f = input("Enter file name : ")
    with open(f,'rt') as ff:
        l=ff.readlines()
        print(l[-1])
except IOError:
        print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")

"""
Code Challenge
  Name: 
    etc passwd
  Filename: 
    passwd.py
  Problem Statement:
    This exercise assumes that you have access to a copy of /etc/passwd,
    The file in which basic user information is stored on Unix computers.
    The format is:

    nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    
    In other words, each line is a set of fields, separated by colon (:) characters. 
    The first field is the username, and the third field is the ID of the user. 
    Thus, on my system, the nobody user has ID -2, the root user has ID 0, 
    and the daemon user has ID 1.  
    You can ignore all but the first and third fields in the file.
    
    There is one exception to this format: 
    A line that begins with a # character is a comment, 
    and should be ignored by the parser.
    
    For this exercise, 
    you must create a dictionary based on /etc/passwd, 
    in which the dict's keys are usernames and the values are the numeric IDs of those users. 
    You should then iterate through this dict, displaying one username and 
    user ID on each line in alphabetical order.
    
"""


users = {} 
with open('data/passwd') as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
for username in sorted(users):
    print("{}:{}".format(username, users[username]))


"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""


try:
    c=0
    w=0
    l=0
    u=0
    f = input("Enter file name : ")
    with open(f,'rt') as ff:
        s = ff.read()
        ss = ''
        for i in s:
            print(i)
            if i != '\n':
                c+=1
                ss +=i
            else:
                l+=1
                ss+=' '
        print(c,l)
        l=ss.split()
        print(len(l))
        print(len(set(l)))
except IOError:
        print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""

from PIL import Image
img = Image.open('a.jpg').convert('LA')
img.save('greyscale.png')
img.show()


img_rotate = img.rotate(90)
img_rotate.show()

width, height = img.size
hw = width/2
hh = height/2

img = img.crop((hw-80,hh-102,hw+80,hh+102))
img.show()

img.thumbnail((75,75))
img.show()

"""
Code Challenge
  Name: 
    Reading and Writing CSV
  Filename: 
    csv.py
  Problem Statement:
    Create a program that reads from one CSV file (/etc/passwd), 
    and writes to another one. 
    
    You are to read from passwd file,
    and produce a file whose contents are the username (index 0) 
    and the user ID (index 2).
    Note that a record may contain a comment, 
    in which it will not have anything at index 2; 
    you should take that into consideration when writing the file.  
    The output file should use TAB characters to separate the elements.
 
    Thus, the input will look like:
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    _ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
    
    and the output will look like:
 
        root    0
        daemon  1
        _ftp    98
    
"""
import csv

with open('data/passwd') as passwd, open('data/output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))

 # Optional 
 
"""
Code Challenge
  Name: 
    SHA-1 Algorithm
  Filename: 
    hash.py
  Problem Statement:
    Find hash of a file using hashlib library and using SHA-1 algorithm
  Hint:
    https://www.programiz.com/python-programming/examples/hash-file
"""

import hashlib
def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("data/romeo.txt")
print(message)


"""
Code Challenge
  Name: 
    Resolution of an Image
  Filename: 
    resolution.py
  Problem Statement:
    Find the resolution of any jpeg Image file ( width x height )
  Hint:
    https://www.programiz.com/python-programming/examples/resolution-image
"""


def jpeg_res(filename):
   
   with open(filename,'rb') as img_file:
       img_file.seek(163)
       a = img_file.read(2)
       
       a_0 = int('.'.join(str(ord(c)) for c in a[0]))
       a_1 = int('.'.join(str(ord(c)) for c in a[1]))
       height = (a_0 << 8) + a_1
       a = img_file.read(2)
       a_0 = int('.'.join(str(ord(c)) for c in a[0]))
       a_1 = int('.'.join(str(ord(c)) for c in a[1]))
       width = (a_0 << 8) + a_1

   print("The resolution of the image is",width,"x",height)

jpeg_res("a.jpg")

"""
Code Challenge
  Name: 
    Different sizes
  Filename: 
    png.py
  Problem Statement:
    Convert all files PNG in a directory into different sizes
  Hint: 
    os.listdir('.') function will list all the files in the current directory   
"""

import os
from PIL import Image

for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, text = os.path.splittext(f)
        i.save('pngs/{}.png'.format(fn))



size_300 = (300,300)
size_700 = (700,700)


for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)
        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))
 
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))











