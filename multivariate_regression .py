#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


wine = pd.read_csv("winequality-red.csv")
wine.shape
wine.head()


# In[8]:


wine.isnull().sum()


# In[9]:


wine.describe()


# In[10]:


wine.info()


# In[12]:


wine.duplicated().sum()


# In[13]:


from pandas_profiling import ProfileReport


# In[8]:


import seaborn as sns


# In[9]:


wine_correlation = wine.corr()
wine_correlation


# In[18]:


axis = sns.heatmap(wine_correlation, vmin = -1, vmax =1,center = 0,cmap = "viridis",square = True )
axis
plt.show()


# In[10]:



newwne = pd.DataFrame(wine.drop(columns = ["quality"]))
for w in newwne:
    fig=plt.figure(figsize = (8,8))
    sns.barplot(x=newwne[w],y=wine["quality"])


# In[11]:


x = newwne
y = wine["quality"]
x.head()


# In[12]:


from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
scalex = scale.fit_transform(x)
scalex


# bins = (2, 6.5, 8)
# group_names = ['bad', 'good']
# wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)

# In[13]:


bins = (2, 6.5, 8)
group_names = ["bad", "good"]
wine["quality"] = pd.cut(wine["quality"], bins = bins, labels = group_names)


# In[14]:


from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder


# In[15]:


label_quality = LabelEncoder()


# In[16]:


wine['quality'] = label_quality.fit_transform(wine['quality'])


# In[17]:


wine['quality'].value_counts()


# In[19]:


sns.countplot(wine["quality"])


# In[27]:


X = wine.drop('quality', axis = 1)
y = pd.factorize(wine['quality'])[0].reshape(-1,1)


# In[23]:


reviews = []
for i in wine['quality']:
    if i >= 1 and i <= 3:
        reviews.append('1')
    elif i >= 4 and i <= 7:
        reviews.append('2')
    elif i >= 8 and i <= 10:
        reviews.append('3')
reviews


# In[ ]:





# In[31]:


from sklearn.preprocessing import Binarizer
bin = Binarizer()
bin.fit_transform(y)


# In[21]:


from sklearn.model_selection import train_test_split
scalex_train,scalex_test,y_train,y_test = train_test_split(scalex, y,test_size = 0.25)


# In[45]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(scalex_train,y_train)
predict = model.predict(scalex_test)
predict


# In[40]:


from sklearn.metrics import accurracy_score
z = accuracy_score(model,predict)
z


# In[47]:


df = pd.DataFrame({'Actual': y_test, 'Predicted': predict})
df

