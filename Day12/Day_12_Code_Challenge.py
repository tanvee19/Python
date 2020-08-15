"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""


import pandas as pd
df = pd.read_csv("training_titanic.csv")
df_rank= df.groupby(['Survived']).size()
print("Survived : ",df_rank[1])
print("Not Survived : ",df_rank[0])
 
df['Survived'].value_counts(normalize = True)

df['Sex'].value_counts(normalize = True)

df_rank=df.groupby(['Survived','Sex'])
print("females :-",len(df_rank.groups[(1,'female')]),':',len(df_rank.groups[(0,'female')]))
print("males :-",len(df_rank.groups[(1,'male')]),':',len(df_rank.groups[(0,'male')]))

df_rank=df.groupby(['Survived','Sex'])


df["bool_Age"] = df['Age'].map(lambda x: 0 if x > 18 else (1 if x<18 else 'a') )
print(len(df.groupby(['Survived','bool_Age']).groups[(0,1)]))
print(len(df.groupby(['Survived','bool_Age']).groups[(1,1)]))

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd
import numpy as np
df = pd.read_csv("Automobile.csv")
df = df['price'].fillna(round(df['price'].mean(),0))
df = np.array(df)
print(df)
print(type(df)) 
print("MIN > ",df.min())

print("Max > ",df.max())

print("Avg > ",np.average(df))

print("Std > ",df.std())


"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
      

import pandas as pd
import numpy as np
datath_df = pd.read_csv("thanksgiving.csv",encoding = "ISO-8859-1")
# Fetching the columns name for further reference
columns_name = list(datath_df.columns)

    # Initializing a code number for each column name
code_col = [x for x in range(0, 65)]

    # Storing the column name with their codes for further reference
columns_ref = dict(zip(code_col, columns_name))

    # Initializing the dataframe with the codes of the column
datath_df.columns = code_col
   # Fetching the data that perform thanksgiving for further processing
datath_df = datath_df[datath_df[1] == "Yes"]

    # Filling out the empty values with 'Mising' keyword
datath_df = datath_df.replace(np.nan, 'Mising')



    # Analysing for the state, area  and income based what is consumed in thankgiving dinner
state_based = datath_df.groupby(64)[2].value_counts().unstack().fillna(0)

income_based = datath_df.groupby(63)[2].value_counts().unstack().fillna(0)

area_based = datath_df.groupby(60)[2].value_counts().unstack().fillna(0)

    # Analysis of the sauces prefered by each incomes group people
sauce_incgrp = datath_df.groupby(8)[63].value_counts().unstack().fillna(0)

    # Filtering the gender and income columns using .apply method
def gender_filter(value):
     if value == "Male":
         value = 'M'
     elif value == "Female":
         value = 'F'
     else:
         pass
     return value

import re
datath_df[62] = datath_df[62].apply(gender_filter)
datath_df[63] = datath_df[63].replace(['Prefer not to answer', 'mising'],['0','0'])
regex = re.compile("\d+\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
def income_filter(value):
     value = regex.findall(value)
     value = [int(x.replace(",", "")) for x in value]
     return sum(value)/(len(value)+0.1)

    # Using the apply method to filter the income column
datath_df[63] = datath_df[63].apply(income_filter)

    # Fetching the average incomes for each type sauces

sauce_compr = datath_df.groupby(8)[63]

sauce_inc = sauce_compr.mean()

    # Visualizing the average income of the various sauces
sauces_inc_visual = sauce_inc.plot.bar()

    # Comparing the incomes of canned and homemade sauces
craneberry_compr = sauce_inc.iloc[[0, 1]]

    # Visualizing the incomes of various craneberry sauces
craneberry_compr_visual = craneberry_compr.plot.pie(autopct="%1.1f%%")

    # Comparing the toufourkey eaten in Suburban and Rural areas
toufurkey_compr = area_based.iloc[[1, 2], [-3]]

    # Visualizing the toufurkey eaten by suburban and rural people
toufurkey_compr.plot.bar(color=["green"])  # yes suburban eat more toufurkey than rural people

    # Checking for a correlation between thankgiving prayer seeker and their income
prayer_inc = datath_df.groupby(51)[63].value_counts().unstack().fillna(0)

    # Visualizing the relation between prayer seeker and their income
prayer_inc_visual = prayer_inc.plot.bar()

    # Analyzing the Blackfriday sales activity
blackfri_sales = datath_df[57].value_counts()
    
pattern_income = datath_df.groupby([2, 8])[63].value_counts().unstack().fillna(0)

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
"""

import pandas as pd

import contextlib as clb

with clb.suppress((FileNotFoundError)):
    churn_df = pd.read_csv("Telecom_churn.csv")

    churned_df = churn_df[churn_df['churn'] == True]

    plans_count = churned_df[(churned_df['international plan'] == 'yes') & (churned_df['voice mail plan'] == 'yes')].shape
    plans_count = plans_count[0]
    print (plans_count)

    call_charge = churn_df.groupby('churn')['total intl charge'].sum()
    visual_1 = call_charge.plot.pie(autopct='%1.1f%%')

    night_call = churned_df['total night minutes'].max()

    call_analysis = churned_df.iloc[:, 7:19].sum().sort_index()
    visual_2 = call_analysis.plot.bar()

    non_churn_al = churn_df['account length'][churn_df['churn'] == False].max()
    churn_al = churned_df['account length'].max()
    if churn_al > non_churn_al:
        print('churned user have the maximum account lenght')
    else:
        print('regular user have the maximum account lenght')

    customer_care = churned_df['customer service calls'].value_counts()

    area_popl = churn_df.groupby('area code')['international plan'].value_counts().unstack()

