#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


std = pd.read_csv("student_scores.csv")


# In[6]:


std.head()


# In[7]:


std.shape


# In[8]:


std.describe


# In[9]:


std.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()


# In[10]:


std.corr()


# In[11]:


x = std.iloc[:, :-1].values


# In[14]:


y = std.iloc[:,1]


# In[15]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


# In[18]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)


# In[20]:


regressor.coef_


# In[22]:


regressor.intercept_


# y = 9,91065648(number of hours)+2.0181600

# In[24]:


y_pred = regressor.predict(x_test)


# In[25]:


y_pred


# In[26]:


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df


# In[27]:


from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[ ]:


np.sqrt(metrics.mean_squared_error(y_test, y_pred))/)

