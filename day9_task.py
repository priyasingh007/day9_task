#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Introduction:
#Pandas is a Python library.
#Pandas is used to analyze data.
#Why Use Pandas?
#Pandas allows us to analyze big data and make conclusions based on statistical theories.
#Pandas can clean messy data sets, and make them readable and relevant.
#Relevant data is very important in data science.


# In[9]:


#Pandas supports two data structures:
#>Series
#>Dataframe
#---------------------------Series----------------------------------
#Pandas is a one-dimensional labeled array and capable of holding data of any type (integer, string, float, python objects, etc.)
#Syntax: pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

#Parameters:

#data: array- Contains data stored in Series.
#index: array-like or Index (1d)
#dtype: str, numpy.dtype, or ExtensionDtype, optional
#name: str, optional
#copy: bool, default False
#Series holding the dictionary.
import pandas as pd
  
dic = { 'Id': 20, 'Name': 'Internity', 
       'State': 'wb','Age': 24}
  
res = pd.Series(dic)
(res)


# In[6]:


#---------------Dataframe--------------------
#Pandas DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes(rows and columns).
# DataFrame can be created using a single list or a list of lists.
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


# In[7]:


#Locate Row
print(df.loc[0])


# In[25]:


#Panel in panda
#pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)


# In[27]:


#panel creation:
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print p


# In[28]:


# Import pandas library
import pandas as pd
  
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age'])
  
# print dataframe.
df


# In[29]:


#Creating Pandas Dataframe from a python objects 
#Creating DataFrame from dict of narray/lists
import pandas as pd
  
# initialise data of lists.
data = {'Name':['Tom', 'Jack', 'nick', 'juli'],
        'marks':[99, 98, 95, 90]}
  
# Creates pandas DataFrame.
df = pd.DataFrame(data, index =['rank1',
                                'rank2',
                                'rank3',
                                'rank4'])
  
# print the data
df


# In[30]:


#Creating Dataframe from list of dicts
import pandas as pd
  
# Initialise data to lists.
data = [{'a': 1, 'b': 2, 'c':3},
        {'a':10, 'b': 20, 'c': 30}]
  
# Creates DataFrame.
df = pd.DataFrame(data)
  
# Print the data
df


# In[36]:


import numpy as np


# In[37]:


# create 4x2 random array 
# array is a list of lists
arr = np.random.rand(4, 2)
arr


# In[42]:


#from a file:
import pandas as pd
  
# creating a data frame
df = pd.read_csv("D:\Downloads\heart.csv")
df


# In[52]:


df.head()


# In[54]:


df.tail()


# In[55]:


df.describe()


# In[56]:


df.info()


# In[57]:


#from api
import requests
import json


# In[58]:


url='https://api.covid19api.com/summary'
r=requests.get(url)
r


# In[59]:


json=r.json()
json


# In[60]:


json.keys()


# In[61]:


json['Global']


# In[62]:


json['Date']


# In[63]:


type(json['Date'])


# In[64]:


type(json['Global'])


# In[ ]:




