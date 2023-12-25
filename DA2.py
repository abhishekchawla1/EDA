#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


data=pd.read_csv(r"C:\Users\ASUS\Downloads\3. Police Data.csv")


# In[3]:


data.isnull().sum()


# In[6]:


data.shape


# In[10]:


data.drop(columns='country_name',inplace=True)


# In[11]:


data


# In[12]:


data.shape


# In[13]:


data.head()


# In[15]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# In[16]:


data[data['violation']=='Speeding'].driver_gender.value_counts()


# In[17]:


data.head(2)


# In[18]:


data.groupby('driver_gender').search_conducted.sum()


# In[19]:


data['search_conducted'].value_counts()


# In[21]:





# In[22]:


data['stop_duration'] = data['stop_duration'].map({'0-15 Min':7.5 , '16-30 Min' : 24 , '30+ Min' : 45})


# In[23]:


data


# In[24]:


data['stop_duration'].mean()


# In[25]:


data


# In[27]:


data.groupby('violation').driver_age.describe()


# In[ ]:




