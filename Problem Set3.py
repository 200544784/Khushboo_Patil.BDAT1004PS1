#!/usr/bin/env python
# coding: utf-8

# # PROBLEM SET 3

# QUESTION 1
# STEP 1 : Import the necessary libraries
# STEP 2 : Import the dataset
# STEP 3 : Assign it to a variable called users.
# STEP 4 : Discover what is the mean age per occupation.
# STEP 5 : Discover the Male ratio per occupation and sort it from the most to the least.
# STEP 6 : For each occupation, calculate the minimum and maximum ages.
# STEP 7 : For each combination of occupation and sex, calculate the mean age.
# STEP 8 : For each occupation present the percentage of women and men

# In[1]:


import pandas as pd


# In[2]:


users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep = "|")
users


# In[3]:


users.groupby("occupation").age.mean()


# In[18]:


# Group by occupation and gender, calculate the percentage of each gender per occupation
genders = users.groupby("occupation")["gender"].value_counts(normalize=True) * 100

genders.head()

gendersn = pd.DataFrame(genders)
gendersn.rename(columns={"gender":"percent"}, inplace=True)

new_gen = pd.DataFrame(gendersn.reset_index(level=["occupation", "gender"]))


# Filter the DataFrame to only include male gender
males = new_gen[new_gen["gender"] == "M"]

# Sort by percentage in descending order
males_sorted = males.sort_values(by="proportion", ascending=False)

males_sorted.head()


# In[19]:


users.groupby("occupation").age.agg([min, max])


# In[20]:


users.groupby(["occupation", "gender"]).age.mean()


# In[21]:


new_gen


# Question 2
# STEP 1 : Import the necessary libraries
# STEP 2 : Import the dataset
# STEP 3 : Assign it to a variable called euro12.
# STEP 4 : Select only the Goal column.
# STEP 5 : How many team participated in the Euro2012?
# STEP 6 : What is the number of columns in the dataset?
# STEP 7 : View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline.
# STEP 8 :  Sort the teams by Red Cards, then to Yellow Cards
# STEP 9 : Calculate the mean Yellow Cards given per Team
# STEP 10 : Filter teams that scored more than 6 goals
# STEP 11 : Select the teams that start with G
# STEP 12 : Select the first 7 columns
# STEP 13 : Select all columns except the last 3.
# STEP 14 : Present only the Shooting Accuracy from England, Italy and Russia
# 

# In[22]:


import pandas as pd


# In[23]:


euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')
euro12


# In[24]:


euro12.Goals


# In[25]:


euro12.shape[0]


# In[26]:


euro12.info()  # Dataset column info


# In[27]:


# filter only giving the column names

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
discipline


# In[28]:


#sorting teams 
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)


# In[29]:


#calculate mean of both the teams 
round(discipline['Yellow Cards'].mean())


# In[30]:


#to see teams having goal more than 6
euro12[euro12.Goals > 6]


# In[31]:


#extract info of team starting with letter G
euro12[euro12.Team.str.startswith('G')]


# In[32]:


#select first 7 columns of dataset
selected_rows = euro12.head(7).iloc[:, 0:7]
selected_rows


# In[34]:


# use negative to exclude the last 3 columns of dataset

euro12.iloc[: , :-3]


# In[37]:


# .loc is another way to slice, using the labels of the columns and indexes

euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


# Question 3 
# STEP 1 : Import the necessary libraries
# STEP 2 : Create 3 differents Series, each of length 100, as follows:
# The first a random number from 1 to 4
# The second a random number from 1 to 3
# The third a random number from 10,000 to 30,000
# STEP 3 :  Let's create a DataFrame by joinning the Series by column
# STEP 4 :  Change the name of the columns to bedrs, bathrs, price_sqr_meter
# STEP 5 :  Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'.
# STEP 6 : Oops, it seems it is going only until index 99. Is it true?
# STEP 7 : Reindex the DataFrame so it goes from 0 to 299

# In[38]:


import pandas as pd
import numpy as np


# In[39]:


x = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
y = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
z = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

print(x ,y, z)


# In[41]:


housing_data = pd.concat([x, y, z], axis=1)
housing_data


# In[42]:


#rename the coulmn name
housing_data.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
housing_data


# In[43]:


# join concat the values
bigcolumn = pd.concat([x, y, z], axis=0)

# it is still a Series, so we need to transform it to a DataFrame
bigcolumn = bigcolumn.to_frame()
print(type(bigcolumn))

bigcolumn


# In[44]:


# define the length of dataframe
len(bigcolumn)


# In[45]:


bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn


# Question 4 
# STEP 1 : Import the necessary libraries
# STEP 2 : Import the dataset from the attached file wind.txt
# STEP 3 : Assign it to a variable called data and replace the first 3 columns by a proper
# datetime index.
# STEP 4 : Year 2061? Do we really have data from this year? Create a function to fix it
# and apply it.
# STEP 5 : Set the right dates as the index. Pay attention at the data type, it should be
# datetime64[ns].
# STEP 6 : Compute how many values are missing for each location over the entire
# record.They should be ignored in all calculations below.
# STEP 7 : Compute how many non-missing values there are in total.
# STEP 8 : Calculate the mean windspeeds of the windspeeds over all the locations and
# all the times.
# A single number for the entire dataset.
# STEP 9 : Create a DataFrame called loc_stats and calculate the min, max and mean
# windspeeds and standard deviations of the windspeeds at each location over all the
# days
# A different set of numbers for each location.
# STEP 10 : Create a DataFrame called day_stats and calculate the min, max and mean
# windspeed and standard deviations of the windspeeds across all the locations at each
# day.
# A different set of numbers for each day.
# STEP 11 : Find the average windspeed in January for each location.
# Treat January 1961 and January 1962 both as January.
# STEP 12 : Downsample the record to a yearly frequency for each location.
# STEP 13 : Downsample the record to a monthly frequency for each location.
# STEP 14 : Downsample the record to a weekly frequency for each location.
# STEP 15 : Calculate the min, max and mean windspeeds and standard deviations of the
# windspeeds across all locations for each week (assume that the first week starts on
# January 2 1961) for the first 52 weeks.

# In[46]:


import pandas as pd
import datetime


# In[48]:


# parse_dates gets 0, 1, 2 columns and parses them as the index
data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(data_url, sep = "\s+", parse_dates = [[0,1,2]]) 
data


# In[49]:


# function that uses datetime
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)


data


# In[50]:


# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])

# set 'Yr_Mo_Dy' with new datatype as the index
data = data.set_index('Yr_Mo_Dy')

data


# In[51]:


#extract null values from each location in dataset

data.isnull().sum()


# In[52]:


#calculate non-missing values for each location 
data.notnull().sum()


# In[53]:


#compute mean windspeeds over all the locations
data.sum().sum() / data.notna().sum().sum()


# In[58]:


#calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location 
loc_stats = data.describe(percentiles=[])
loc_stats


# In[59]:


# create the dataframe
day_stats = pd.DataFrame()

# this time we determine statistical description of windspeed at each day
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max 
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

day_stats.head()


# In[60]:


data.loc[data.index.month == 1].mean()


# In[61]:


data.groupby(data.index.to_period('A')).mean()


# In[62]:


data.groupby(data.index.to_period('M')).mean()


# In[63]:


data.groupby(data.index.to_period('W')).mean()


# In[64]:


weekly = data.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10)


# Question 5
# STEP 1 : Import the necessary libraries
# STEP 2 : Import the dataset 
# STEP 3 : Assign it to a variable called chipo
# STEP 4 : See the first 10 entries
# STEP 5 : What is the number of observations in the dataset?
# STEP 6 : What is the number of columns in the dataset?
# STEP 7 : Print the name of all the columns
# STEP 8 : How is the dataset indexed?.
# STEP 9 : Which was the most-ordered item?
# STEP 10 : For the most-ordered item, how many items were ordered?
# STEP 11 : What was the most ordered item in the choice_description column?
# STEP 12 : How many items were orderd in total?
# STEP 13 : Turn the item price into a float
# a. Check the item price type
# b. Create a lambda function and change the type of item price
# c. Check the item price type
# STEP 14 : How much was the revenue for the period in the dataset?
# STEP 15 : How many orders were made in
# STEP 16 : What is the average revenue amount per order?
# STEP 17 : How many different items are sold?
# 

# In[65]:


import pandas as pd


# In[66]:


chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')


# In[67]:


chipo


# In[68]:


chipo.head(10)


# In[69]:


#information about number of observation
chipo.info()


# In[70]:


#cloumns info
chipo.shape[1]


# In[71]:


#name of columns
chipo.columns.values


# In[72]:


#dataset index
chipo.index


# In[75]:


#most ordered item
chipo.groupby('item_name').sum().sort_values(['quantity'], ascending=False).head(1)


# In[76]:


#show how many items were ordered for most order item
chipo.groupby(['item_name']).quantity.sum().sort_values(ascending = False).values[0]


# In[77]:


#the most ordered item in the choice_description column?
chipo.groupby(['choice_description']).quantity.sum().sort_values(ascending = False).index[0]


# In[78]:


# items were orderd in total?
chipo.quantity.sum()


# In[79]:


#a. Check the item price type
chipo.dtypes.item_price
#b. Create a lambda function and change the type of item price
chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))
chipo.item_price
#c. Check the item price type
chipo.item_price.dtypes


# In[83]:


chipo['revenue'] = chipo['quantity']*chipo.item_price
revenue = chipo.revenue.sum()
revenue


# In[81]:


# compute how many orders were made in the period
total_order = chipo.order_id.nunique()
total_order


# In[84]:


#calculate average of both
revenue/total_order


# In[85]:


chipo.item_name.value_counts().count()


# Question 6 
# Create a line plot showing the number of marriages and divorces per capita in the
# U.S. between 1867 and 2014. Label both lines and show the legend.
# Don't forget to label your axes!

# In[89]:


import pandas as pd
import matplotlib.pyplot as plt

us_marriage_divorce_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
years = us_marriage_divorce_data['Year'].values
marriages_per_capita = us_marriage_divorce_data['Marriages_per_1000'].values
divorces_per_capita = us_marriage_divorce_data['Divorces_per_1000'].values

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, marriages_per_capita, label='Marriages per 1000', marker='o')
plt.plot(years, divorces_per_capita, label='Divorces per 1000', marker='o')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Per Capita Rate')
plt.title('Number of Marriages and Divorces per Capita in the U.S. (1867-2014)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


# Question 7
# Create a vertical bar chart comparing the number of marriages and divorces per
# capita in the U.S. between 1900, 1950, and 2000.

# In[90]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
us_marriage_divorce_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')

# Select data for the years 1900, 1950, and 2000
selected_years = [1900, 1950, 2000]
selected_data = us_marriage_divorce_data[us_marriage_divorce_data['Year'].isin(selected_years)]

# Plotting
plt.figure(figsize=(10, 6))
bar_width = 0.35

# Create bars for marriages
plt.bar(selected_data['Year'] - bar_width/2, selected_data['Marriages_per_1000'],
        width=bar_width, label='Marriages per 1000', align='center')

# Create bars for divorces
plt.bar(selected_data['Year'] + bar_width/2, selected_data['Divorces_per_1000'],
        width=bar_width, label='Divorces per 1000', align='center')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Per Capita Rate')
plt.title('Comparison of Marriages and Divorces per Capita in the U.S. (1900, 1950, 2000)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


# Question 8
# Create a horizontal bar chart that compares the deadliest actors in Hollywood. Sort the actors by their kill count and label each bar with the corresponding actor's name.

# In[91]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
hollywood_actor_kills = pd.read_csv('actor_kill_counts.csv')

# Sort the data by kill count in descending order
sorted_data = hollywood_actor_kills.sort_values(by='Count', ascending=True)

# Plotting
plt.figure(figsize=(10, 6))

# Create a horizontal bar chart
plt.barh(sorted_data['Actor'], sorted_data['Count'], color='skyblue')

# Adding labels and title
plt.xlabel('Kill Count')
plt.ylabel('Actor')
plt.title('Deadliest Actors in Hollywood')

# Show the plot
plt.grid(axis='x')
plt.show()


# Question 9
# Create a pie chart showing the fraction of all Roman Emperors that were assassinated.
# 
# Make sure that the pie chart is an even circle, labels the categories, and shows the percentage breakdown of the categories

# In[92]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
roman_emperors = pd.read_csv('roman-emperor-reigns.csv')

# Count the number of assassinated emperors
assassinated_emperors = roman_emperors[
    roman_emperors['Cause_of_Death'].apply(lambda x: 'assassinated' in x.lower())]

number_assassinated = len(assassinated_emperors)
other_deaths = len(roman_emperors) - number_assassinated

# Data for the pie chart
labels = ['Assassinated Emperors', 'Other Deaths']
sizes = [number_assassinated, other_deaths]

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'lightgray'])

# Adding title
plt.title('Fraction of Roman Emperors Assassinated')

# Show the plot
plt.show()


# Question 10
# Create a scatter plot showing the relationship between the total revenue earned by arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009.

# In[93]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
arcade_revenue_cs_doctorates = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')

# Extract data for the scatter plot
arcade_revenue = arcade_revenue_cs_doctorates['Total Arcade Revenue (billions)'].values
cs_doctorates_awarded = arcade_revenue_cs_doctorates['Computer Science Doctorates Awarded (US)'].values

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(arcade_revenue, cs_doctorates_awarded, color='blue', alpha=0.7)

# Adding labels and title
plt.xlabel('Total Arcade Revenue (billions)')
plt.ylabel('Computer Science Doctorates Awarded (US)')
plt.title('Relationship Between Arcade Revenue and CS Doctorates (2000-2009)')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:




