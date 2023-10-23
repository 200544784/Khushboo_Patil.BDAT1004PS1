#!/usr/bin/env python
# coding: utf-8

# # Problem Set 2

# Question 1 

# In[4]:


a = 0
def b():
    global a 
    a = c(a)
    
def c(a):
    return a + 2


# In[5]:


b()


# In[6]:


b()


# In[7]:


b()


# In[8]:


a


# Value of a as output we get 6 
# Explanation of code -
# Firstly a is initialized as 0 next is function b() that uses the global keyword to indicate that it will use the global variable a,and second function c(a) that takes a parameter a and returns the value of a + 2.
# 
# Inside b(), a is assigned the result of calling c(a). This means it will update the global variable a by adding 2 to its current value.And when we call function b() three times value of a is added accordingly by giving us as output 6

# Question 2

# In[ ]:


def filelength(file_name):
    
    try:
        file = open(file_name)     #Open the file
        contents = file.read()     #Read the contents
        file.close() #close the file
        print(len(contents)) #print the length of file
        
    except FileNotFoundError:
        
       return f"{file_name} File not found in system"  #prints the exception if file is not found
        
        


# In[13]:


file_name = "currencies.txt" 
filelength(file_name)


# In[20]:


file_name = "txt1.py"
filelength(file_name)


# Question 3

# In[21]:


class Marsupial:
    def __init__(self):
        # Initialize an empty list to represent the pouch contents
        self.pouch = []

    def put_in_pouch(self, item):
        # Add the item to the pouch
        self.pouch.append(item)

    def pouch_contents(self):
        # Return the contents of the pouch
        return self.pouch
    
    


# In[ ]:


m = Marsupial()


# In[23]:


m.put_in_pouch('doll')


# In[24]:


m.put_in_pouch('firetruck')


# In[25]:


m.put_in_pouch('kitten')


# In[26]:


m.pouch_contents()


# In[46]:


class Kangaroo(Marsupial):
    def __init__(self,x, y):  
        super().__init__()
        self.x = x
        self.y = y

    def jump( self,dx, dy):  
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"I am Kangaroo located at coordinates ({self.x}, {self.y})"




# In[47]:


k = Kangaroo(0,0)


# In[48]:


print(k)


# In[49]:


k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()


# In[50]:


k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# Question 4

# In[63]:


def collatz(x): #If x is equal to 1, the function returns, indicating the end of the sequence. Otherwise, it checks if x is even (divisible by 2)  If x is even, the function calls itself recursively with x divided by 2 (x // 2). If x is odd, the function calls itself recursively with 3 * x + 1. This process continues until x reaches 1
    print(x)
    if x == 1:
        return
    elif x // 2 == 0:
        collatz(x // 2)
    else:
        collatz(3 * x + 1)


# In[60]:


collatz(10)


# In[64]:


collatz(1)


# Question 5

# In[2]:


def binary(n):
    if n > 1:
        binary(n // 2)
    print(n % 2, end='')


binary(10)


# In[3]:


binary(2)


# Question 6 #refernce https://docs.python.org/3/library/html.parser.html

# In[21]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag and tag[0] == 'h' and len(tag) > 1 and tag[1].isdigit():
            self.indentation = int(tag[1]) - 1

    def handle_data(self, data):
        if hasattr(self, 'indentation') and self.indentation >= 0:
            print(' ' * self.indentation + data)




# In[22]:


infile = open('w3c.html') 
content = infile.read() 
infile.close() 
hp = HeadingParser()
hp.feed(content)


# In[27]:


pip install beautifulsoup4


# Question 7 #reference https://www.geeksforgeeks.org/python-program-to-recursively-scrape-all-the-urls-of-the-website/

# In[12]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def webdir(url, depth, indent=0):
    # Base case: depth is 0
    if depth == 0:
        return

    # Get the web page content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the URL with indentation
    print(' ' * indent + url)

    # Find all the links on the web page
    links = soup.find_all('a')

    # Recursive call for each link
    for link in links:
        href = link.get('href')
        parsed_url = urlparse(href)
        if parsed_url.scheme:
            webdir(href, depth - 1, indent + 4)









# In[13]:


webdir('https://docs.python.org/3/library/html.parser.html',2,0)


# Question 8 #refernce https://www.geeksforgeeks.org/python-sqlite-select-data-from-table/

# In[19]:


import sqlite3

# Create a connection to the database
conn = sqlite3.connect('city_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store city details 
cursor.execute('''CREATE TABLE cityInfo (
                    CityName TEXT,
                    Country TEXT,
                    Season TEXT,
                    Temperature REAL,
                    Rainfall REAL
                )''')

# Insert data into the table
cursor.execute("INSERT INTO cityInfo VALUES ('Mumbai', 'India', 'Winter', 24.8, 5.9)")
cursor.execute("INSERT INTO cityInfo VALUES ('Mumbai', 'India', 'Spring', 28.4, 16.2)")
cursor.execute("INSERT INTO cityInfo VALUES ('Mumbai', 'India', 'Summer', 27.9, 1549.4)")
cursor.execute("INSERT INTO cityInfo VALUES ('London', 'United Kingdom', 'Winter', 4.2, 346.0)")
cursor.execute("INSERT INTO cityInfo VALUES ('London', 'United Kingdom', 'Spring', 8.3, 207.7)")
cursor.execute("INSERT INTO cityInfo VALUES ('London', 'United Kingdom', 'Summer', 15.7, 169.6)")
cursor.execute("INSERT INTO cityInfo VALUES ('London', 'United Kingdom', 'Fall', 27.6, 157.0)")
cursor.execute("INSERT INTO cityInfo VALUES ('Cairo', 'Egypt', 'Winter', 10.4, 218.5)")
cursor.execute("INSERT INTO cityInfo VALUES ('Cairo', 'Egypt', 'Spring', 13.6, 16.5)")
cursor.execute("INSERT INTO cityInfo VALUES ('Cairo', 'Egypt', 'Summer', 20.7, 6.5)")
cursor.execute("INSERT INTO cityInfo VALUES ('Cairo', 'Egypt', 'Fall', 27.7, 0.1)")

# Commit the changes to the database
conn.commit()



print("Table is created")

# Close the connection
conn.close()




# In[49]:


import sqlite3

# Create a connection to the database
conn = sqlite3.connect('city_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# A) All the temperature data.
cursor.execute("SELECT Temperature FROM cityInfo")

# Fetch all the temperature data
temperature_data = cursor.fetchall()

# Print the temperature data
print("A) All the Details of Temperature from Database:")
for temp in temperature_data:
    print(temp[0])
    
# B) All the cities, but without repetition.

cursor.execute("SELECT DISTINCT CityName FROM cityInfo")
city_name = cursor.fetchall()

# Print the temperature data
print("B)  All the Distinct City Name from Database:")
for cityName in city_name:
    print(cityName[0])
# C) All the records for India:
cursor.execute("SELECT * FROM cityInfo WHERE Country = 'India'")
india = cursor.fetchall()

print("C) All details of India")

# Print column headers
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("CityName", "Country", "Season", "Temperature", "Rainfall"))

# Print each row
for row in india:
    city_name, country, season, temperature, rainfall = row
    
    print(" {:<15} {:<15} {:<15} {:<15} {:<15}".format(city_name, country, season, temperature, rainfall))
#  D) All the Fall records:
cursor.execute("SELECT * FROM cityInfo WHERE Season = 'Fall'")
fall = cursor.fetchall()

print("D) All records of FALL season")

# Print column headers
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("CityName", "Country", "Season", "Temperature", "Rainfall"))

# Print each row
for row in fall:
    city_name, country, season, temperature, rainfall = row
    
    print(" {:<15} {:<15} {:<15} {:<15} {:<15}".format(city_name, country, season, temperature, rainfall))
    

# E) The city, country, and season for which the average rainfall is between 200 and 400 millimeters:
cursor.execute("SELECT CityName, Country, Season, AVG(Rainfall) AS AvgRainfall FROM cityInfo GROUP BY CityName, Country, Season HAVING AvgRainfall BETWEEN 200 AND 400")
rainfall = cursor.fetchall()

print("E) All records of Average Rainfall")

# Print column headers
print("{:<15} {:<15} {:<15} {:<15} ".format("CityName", "Country", "Season", "AvgRainfall"))

# Print each row
for row in rainfall:
    city_name, country, season, avg_rainfall = row
    
    print(" {:<15} {:<15} {:<15} {:<15} ".format(city_name, country, season, avg_rainfall))

# F) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
cursor.execute("""
    SELECT CityName, Country, 'Fall' AS Season, AVG(Temperature) AS AvgTemperature
    FROM cityInfo
    WHERE Season = 'Fall'
    GROUP BY CityName, Country
    HAVING AvgTemperature > 20
    ORDER BY AvgTemperature ASC
""")

# Fetch all the rows and store them in a variable
temperature = cursor.fetchall()
print("F) All records of Average Temperature in Fall Season")

# Print column headers
print("{:<15} {:<15} {:<15} {:<15}".format("CityName", "Country", "Season", "AvgTemperature"))

# Print each row
for temp in temperature:
    city_name, country, season, avg_temperature = temp
    print("{:<15} {:<15} {:<15} {:<15}".format(city_name, country, season, avg_temperature))

    
# G) The total annual rainfall for Cairo.
cursor.execute("SELECT CityName, SUM(Rainfall) AS total_rainfall FROM cityInfo WHERE  CityName = 'Cairo'")

# Fetch and print the results
results = cursor.fetchall()
print("G) total annual rainfall for Cairo ")
for row in results:
    print(f"{row[0]}: {row[1]} mm")
    
# H) The total rainfall for each season.

cursor.execute("SELECT Season, SUM(Rainfall) FROM cityInfo GROUP BY Season")
season_rainfall = cursor.fetchall()
print("H) total  rainfall per season ")
# Print the results
for season, rainfall in season_rainfall:
    print(f'Total rainfall for {season}: {rainfall} mm')




# Close the connection
conn.close()










# Question 9 

# In[14]:


list_data = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# a) Uppercase version of each word
ucase_words = [word.upper() for word in list_data]
print(ucase_words)

# b) Lowercase version of each word
lcase_words = [word.lower() for word in list_data]
print(lcase_words)

# c) Length of each word
word_length = [len(word) for word in list_data]
print(word_length)

# d) List containing uppercase, lowercase, and length of each word
word_details = [[word.upper(), word.lower(), len(word)] for word in list_data]
print(word_details)

# e) Words with 4 or more characters
long_words = [word for word in list_data if len(word) >= 4]
print(long_words)


# In[ ]:




