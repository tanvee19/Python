
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt


wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")

all_tables=soup.find_all('table')
right_table=soup.find('table', class_='wikitable sortable')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 7:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())


col_name = ["Rank","State or UN","Area","Region","NationalShare","Land Mass","Ref"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("Data.csv")

df = df.head(6)

labels = df['State or UN']
sizes = df['NationalShare']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','black']
explode = (0.1, 0, 0, 0, 0, 0) 

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)



"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Automobile.csv")
df = df['make'].value_counts()
labels = df.index[:10]
sizes = df.values[:10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','black','purple','red','white','silver']
explode = (0.1, 0, 0, 0, 0, 0,0,0,0,0) 

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""

import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
import os

df = pd.DataFrame()
for file in os.listdir("baby_names"):
    if file.endswith('.txt'):
        file = "baby_names\\"+file
        df1 = pd.read_csv(file,header = None)
        df1["year"] = file[14:18]
        df = pd.concat([df,df1])



import pandas as pd
l1 = []
df = pd.DataFrame()
for i in range(1880,2011):
    str1 = 'yob'+str(i)+".txt"
    with open(str1) as file:
        data = file.read().splitlines()
    df[i] = pd.Series(data)





"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""


import pandas as pd

import numpy as np

from collections import Counter

try:

    json_df = pd.read_json("usagov_bitly_data.json", lines=True)

    json_df = json_df.replace([np.nan, ""], ["Mising", "Unknown"])

    json_df_tz = json_df['tz'].value_counts().head(10)

    json_tz = Counter(json_df['tz'])

    json_tz = sorted(json_tz.items(), key=lambda x: x[1], reverse=True)

    json_tz = json_tz[:10]

    tz_count = json_df['tz'].value_counts()

    json_df_tz.plot.bar()

    tokens_df = json_df['a'].str.split(n=1, expand=True).add_prefix("Token_")
    tokens_frequency = tokens_df['Token_0'].value_counts()

    tokens_frequency.head().plot.bar()

    tokens_df = tokens_df.replace(np.nan, 'Mising')

    tokens_df["os"] = 'Not Windows'

    tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"

except ValueError as e:
    print(e)

except AttributeError as e:
    print(e)

except TypeError as e:
    print(e)

"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))



"""
import pandas as pd

import numpy as np

df = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv',header=0)


df['AnnualSalary'] = df['AnnualSalary'].astype(str)

df['AnnualSalary'].apply(lambda x: x.replace('$',''))

df['AnnualSalary'] = df['AnnualSalary'].astype(float)



# group the data
grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])


output = df.sort_values(['AnnualSalary'],ascending=0)
print (str(output.iloc[0,0])+" get the highest salary")


grouped = df.groupby(['JobTitle'])
sorted(grouped.keys())

# Top 10 jobroles according to employees numbers
df['JobTitle'].value_counts()[0:10].plot('bar')

#  which Job Title spends the most
aggregated.sort_values(['sum'],ascending=0,inplace=True)
print (str(aggregated.index[0])+" job title spends the most")

aggregated['sum'][0:10].plot('bar')

# List All the Agency ID and Agency Name
agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)

# Find all the missing Gross data in the dataset
df['GrossPay'].isnull().sum()


"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv("ign.csv")
xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
