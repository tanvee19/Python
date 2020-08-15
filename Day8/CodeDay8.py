# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:25:47 2019

@author: Tanvee
"""


"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from bs4 import BeautifulSoup
source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print(source)
soup = BeautifulSoup(source,"lxml")
all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_="table")

print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.find_all('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
print(A)

import pandas as pd
from collections import OrderedDict

col_name = ["Pos","Team","wght matches","points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
dfe = pd.DataFrame(col_data) 
dfe.to_csv("test.csv")




"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
 
from selenium import webdriver   
wiki = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:\Users\Tanvee\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(wiki)    

right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("sele.csv")

driver.quit()


"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

import requests

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
with open("forsk-logo.png","wb") as f:
    f.write(response.content)
    
    
    