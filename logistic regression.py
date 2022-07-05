#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


heart_disease = pd.read_csv("framingham_heart_disease.csv")
heart = pd.DataFrame(heart_disease)
heart.describe()


# In[18]:


heart.isnull().sum()


# In[9]:


heart.drop(columns = ["education"],inplace = True)


# In[48]:


cigsperday = heart["cigsPerDay"]
x = cigsperday.mean()
x


# In[49]:


heart["cigsPerDay"].fillna(x, inplace = True)


# In[50]:


y = heart["BPMeds"].mean()
heart["BPMeds"].fillna(y,inplace = True)


# In[51]:


z = heart["totChol"].mean()
heart["totChol"].fillna(z,inplace = True)


# In[52]:


a = heart["BMI"].mean()
heart["BMI"].fillna(a, inplace = True)


# In[54]:


b = heart["heartRate"].mean()
heart["heartRate"].fillna(b, inplace = True)


# In[55]:


c = heart["glucose"].mean()
heart["glucose"].fillna(c, inplace = True)


# In[19]:


heart.TenYearCHD.value_counts()


# In[20]:


from pandas_profiling import ProfileReport


# In[21]:


profile = ProfileReport(heart, title = "pandas profiling report", explorative = True)
profile


# In[60]:



x=heart[["male","age","cigsPerDay","BPMeds","prevalentStroke","prevalentHyp","diabetes","BMI","totChol","sysBP","glucose",]]
y = heart["TenYearCHD"]


# In[4]:


from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
scalex = scale.fit_transform(x)
scalex


# In[3]:



from sklearn.model_selection import train_test_split
scalex_train,scalex_test,y_train,y_test=train_test_split(scalex, y, test_size = 0.2)


# In[2]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(scalex_train, y_train)
predict = model.predict(scalex_test)
predict()


# In[72]:


from sklearn.metrics import accurracy_score
z = accuracy_score(y_test,predict)
z


# 
