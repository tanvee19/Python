# -*- cod(ing: utf-8 -*-
"""
Created on Fri May 17 09:05:55 2019

@author: Tanvee
"""

"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""


input1 = int(input(" > "))
i = str(input(" > "))

"""

Code Challenge 2

I-Card Generation System

Write a Python code for a system that generates I-card for all studentsof Forsk
Summer Developer Program and store them in image format. 

It must take names and other required information from the user.
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def id_gen(image,str1,str2):
    img = Image.new(mode='RGBA',size=(300,380),color = (255,255,255,255))
    pic = Image.open("Forsk_logo.png")
    W,H=img.size
    pic.thumbnail((300, 400))
    img.paste(pic,(0,0))
    imga = Image.open(image)
    imga.thumbnail((150,150))
    img.paste(imga,(75,130))
    
    draw = ImageDraw.Draw(img)
    black = (3,8,12)
    font = ImageFont.truetype("arial.ttf",30)
    w,h = font.getsize(str1)
    draw.text(((W-w)/2,280),str1,fill=black,font=font)
    
    font = ImageFont.truetype("arial.ttf",20)
    w,h = font.getsize(str2)
    draw.text(((W-w)/2,315),str2,fill=black,font=font)


    img.show()
    
id_gen("Tanvee.jpg","Tanvee Gupta","FSDP2019/000")


"""

Code Challenge 3

Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def watermark_text(inputi,outputi,text,pos):
    pic = Image.open(inputi)
    draw = ImageDraw.Draw(pic)
    black = (3,8,12)
    font = ImageFont.truetype("arial.ttf",40)
    draw.text(pos,text,fill=black,font=font)
    pic.show()
    pic.save(outputi)
  
def watermark_img(inputi,output,imgpath,pos):
    pic = Image.open(inputi)
    watermark = Image.open(imgpath)
    watermark.thumbnail((150, 100))
    pic.paste(watermark,pos)
    pic.show()
    pic.save(output)
  
watermark_text("Tanvee.jpg","Tanu.jpg",text = "Perfectly Imperfect",pos = (0,0))

watermark_img("Tanvee.jpg","Tanu1.jpg","a.jpg",pos = (0,0))

"""


Code Challenge 4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""





"""


Code Challenge 5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Tweeter account
 of the user.



"""

import pandas as pd
from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
source = requests.get("https://www.drikpanchang.com/astrology/prediction/info/find-rashi-with-name.html").text

soup = BeautifulSoup(source,"lxml")
alldiv=soup.find_all('div')

rightdiv=soup.find('div', class_="dpGroup dpFlexWrap")

#print (rightdiv)
all_a=rightdiv.find_all('a')
#print(all_a)

A=[]
B=[]
for row in rightdiv.find_all('a'):
    cells = row.find_all('span',class_="dpElementKey")
    for item in row.find_all('span',class_="dpElementValue"):
        rows = row.find_all('strong')
    A.append(cells[0].text.strip())
    B.append(rows[0].text.strip())

print(A)
print(B)

col_name = ["Rashee","Alphabets"]
col_data = OrderedDict(zip(col_name,[A,B]))
fe = pd.DataFrame(col_data) 
fe.to_csv("Horo.csv")
















