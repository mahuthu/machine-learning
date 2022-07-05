#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import  pandas as pd
movies = pd.read_csv("IMDB-Movie-Data.csv")
movies


# In[2]:


movies.shape


# In[3]:


movies.info()


# In[4]:


#handling duplicates
ten_df = movies.append(movies)
ten_df.head()


# In[5]:


ten_df.shape


# In[6]:


ten_df.drop_duplicates(inplace = True)
#you can pas in another argument keep
#1 first(default)


# In[7]:


ten_df.shape


# In[9]:


movies.columns


# In[10]:


movies.rename(columns = {
    "Runtime (Minutes)" : "Runtime",
    "Revenue (Millions)": "Revenue"
}, inplace = True)
movies.columns


# In[11]:


#renaming columns in lower case
#using for loops
new_column = []
for x in movies.columns:
    new_column.append(x.lower())
movies.columns = new_column


# In[ ]:


#using map function
movies.columns = List(map(str.lower,movies.columns))


# In[ ]:


#using list comprehension
movies.columns = [col.upper() for col in movies]
movies


# In[12]:


#dealing with missing values
#how to get rid of rows,columns with nulls
#how to replace nulls with non nulls
movies.isnull().head()


# In[16]:


#sum of null values in columns
movies.isnull().sum()


# In[17]:


revenue = movies["revenue"]
revenue.head()


# In[18]:


#replace the null values with hte mean
revenue_mean = revenue.mean()
revenue_mean


# In[30]:


revenue.fillna(revenue_mean,inplace = True)


# In[20]:


#movies.dropna(inplace = True)


# In[31]:


movies.info()


# In[22]:


movies.columns


# In[23]:


metascore = movies["metascore"]
metascore_mean = metascore.mean()
metascore_mean


# In[24]:


movies["genre"].describe()


# In[28]:


movies["genre"].value_counts().head(n = 180)


# In[26]:


x = movies[["genre","rating"]]
x.head()


# In[32]:


movies.head(2)


# 

# In[33]:


movies.to_csv("test24th.csv")


# In[ ]:




