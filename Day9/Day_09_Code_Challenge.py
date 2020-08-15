
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""


from pandas import DataFrame
import mysql.connector
conn = mysql.connector.connect(user='tanvee', password='12345678',
                              host='db4free.net', database = 'database198')
c = conn.cursor()
c.execute("DROP Table db_University;")
c.execute ("""CREATE TABLE db_University(
          Student_Name TEXT,
          Student_age  INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")
c.execute("INSERT INTO db_University VALUES ('Sylvester',25,112,'cs')")
c.execute("INSERT INTO db_University VALUES ('Yogendra', 23,114,'ec')")
c.execute("INSERT INTO db_University VALUES ('Rohit', 26,115,'mec')")
c.execute("INSERT INTO db_University VALUES ('Kunal',19,116,'ee')")
c.execute("INSERT INTO db_University VALUES ('Devendra', 23,116,'ee')")
c.execute("INSERT INTO db_University VALUES ('Sylves', 22,117,'cs')")
c.execute("INSERT INTO db_University VALUES ('Yogendra',21,121,'ec')")
c.execute("INSERT INTO db_University VALUES ('Rohit', 24,118,'cse')")
c.execute("INSERT INTO db_University VALUES ('Kunal',25,119,'cse')")
c.execute("INSERT INTO db_University VALUES ('Devendra', 25,120,'cs')")

c.execute("SELECT * FROM db_University ")
print ( c.fetchall() )


"""

Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.


Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""

from pandas import DataFrame
import mysql.connector
conn = mysql.connector.connect(user='tanvee', password='12345678',
                              host='db4free.net', database = 'database198')
c = conn.cursor()
c.execute("DROP Table bidplus;")
c.execute ("""CREATE TABLE bidplus(
          BID_NO INTEGER,
          items TEXT,
          Quantity Required INTEGER,
          Address TEXT,
          Start TEXT,
          End TEXT
          )""")
c.execute("INSERT INTO bidplus VALUES ()")
c.execute("INSERT INTO bidplus VALUES ()")
c.execute("INSERT INTO bidplus VALUES ()")
c.execute("INSERT INTO bidplus VALUES ()")

c.execute("SELECT * FROM bidplus")
print ( c.fetchall() )




"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""