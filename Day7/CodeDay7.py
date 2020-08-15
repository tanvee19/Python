# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:30:40 2019

@author: Tanvee
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json
import requests
json_input = """[{'First Name' : 'Tanvee',
'Last Name' : 'Gupta',
'Photo' : null,
'Department' : 'CS',
'Research Areas' : ['os','ppl'],
'Contact Details' : 7890456455},
{'First Name' : 'Tanu',
'Last Name' : 'Gupta',
'Photo' :null,
'Department' : 'Cv',
'Research Areas' : 'ppl',
'Contact Details' : 7890456455}]
"""

with open("data_file.json", "w") as write_file:
    json.dump(json_input, write_file)
    # json.dump(json_string, write_file, indent=2   )

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

from datetime import datetime
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
print(response.content)
jsondata = response.json()
print(jsondata)
print('long : '+str(jsondata['coord']['lon']))
print('lat : ' + str(jsondata['coord']['lat']))
print('weather : ' ,jsondata['weather'][0]['main'])
print('wind : ' ,jsondata['wind']['speed'])
print('sun rise set : ', datetime.fromtimestamp(jsondata['sys']['sunrise']).strftime('%H:%M:%S')+'AM', jsondata['sys']['sunset'])




"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

url = "https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=819d286f35199b509b4b"
    
print (url)


response1 = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
print(response1.content)
jsondata1 = response1.json()
input1 = float(input("Enter inr value "))
print(jsondata1['USD_PHP']*input1)

