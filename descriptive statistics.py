#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
movies = pd.read_csv("test24th.csv",index_col = "rank")
movies


# In[8]:


movies.info()


# In[9]:


movies.shape


# In[13]:


movies.info()


# In[5]:


movies.head(2)


# ### 1. Data Wrangling(check there're any null values,duplicates,data format -utf-8 encoded)
# ##### measures of Central tendencies
# * mean(continous variable i.e sales,income..)
# * mode (count/categrical variable i.e gender)
# * median (middle value,when sorted,ordinal data numeric)
# ##### Dropping an entire column/row
# * More than 40% of values missing. So as not biasness.
# #### NB: Take not to loose so much data which might cause underfit in your modelling
# * Sampling - Random,cluster sampling... How many samples you would take for you righ inference. at least > 8% population.
# ### 2 .Descriptive Statistics (Exploratory Data Analysis - EDA)
# ##### Get to explain your data with Frequency tables - distributed mct, variation (standard deviation/variance) and ##### Visualizations (Charts) 
# * Pie chart - Categorical data with less than 10 categroies,gender.
# * Bar/Column chart - Categrorical data with many categroies.
# * Line chart - Time series data. Data collected over time.Trend.
# 
# * Scatter plot - Data points are spread out. Trend.
# * Box plot - Outliers, Max, Min, 75th Percentile,25th Percentile, Mean/Median.
# * Histogram - Frequency(count) distribution of sorted data. Perfectly normally distributed will form a bell shaped histrogram.
# ##### Data normalization 
# * Normally skewed
# * Skewness Right/Left
# 
# #### Kurtosis

# In[14]:


movies.describe()


# In[17]:


movies["genre"].describe()


# ### Correlation explaining the relationship between continous varibales. Correlation coeffecient is a value between 0 and 1 (0 and 100%).
# * 0 - 0.3 (Low correlation)
# * 0.31 - 0.55 (Average correlation)
# * 0.56 - 1 (Strong correlation)
# 
# * Positive correlation - when one goes up the other goes up. When one goes down,the other goes down.
# * Negative correlation- the  go different directions.
# 
# ###### .75 E.g Sales and Marketing have a strong positive correlation
# ###### -0.34 E.g Price and sales have a negative correlation.

# In[18]:


movies.corr()


# In[ ]:




