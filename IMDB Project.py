#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all necessary files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sen


# In[2]:


#importing the 
movies = pd.read_csv(r'C:\Users\hp\Desktop\IMDB Data set\movie.csv')
print(movies)


# In[3]:


movies.columns


# In[4]:


movies.isnull()


# In[5]:


movies.isnull().sum()


# In[6]:


ratings = pd.read_csv(r'C:\Users\hp\Desktop\IMDB Data set\rating.csv')
print(ratings)


# In[7]:


ratings.columns


# In[8]:


ratings.shape


# In[9]:


tags = pd.read_csv(r'C:\Users\hp\Desktop\IMDB Data set\tag.csv')
tags.shape
tags.columns


# In[10]:


del ratings ['timestamp']


# In[11]:


del tags ['timestamp']


# In[12]:


tags.columns


# In[13]:


row_0 = tags.iloc[0]
type(row_0)


# In[14]:


print(row_0)


# In[15]:


row_0.index


# In[16]:


row_0.index


# In[17]:


row_0['userId']


# In[18]:


'rating' in row_0


# In[19]:


row_0.name


# In[20]:


'rating' in row_0


# In[21]:


row_0 = row_0.rename('firstRow')
row_0.name


# In[22]:


tags.head()


# In[23]:


tags.index


# In[24]:


tags.columns


# In[25]:


tags.iloc[ [0,11,500,999] ]


# In[26]:


ratings['rating'].describe()


# In[27]:


ratings.describe()


# In[28]:


ratings['rating'].mean()


# In[29]:


ratings.mean()


# In[30]:


ratings['rating'].min()


# In[31]:


ratings.min()


# In[32]:


ratings['rating'].max()


# In[33]:


ratings['rating'].std()


# In[34]:


ratings['rating'].mode()


# In[35]:


ratings.corr()


# In[51]:


filter1 = ratings['rating'] > 10
print(filter1)
filter1.any()


# In[53]:


filter2 = ratings['rating'] > 0
filter2.all()


# In[54]:


movies.shape


# In[61]:


movies.isnull().any().any()


# In[56]:


ratings.shape


# In[62]:


ratings.isnull().any().any()


# In[63]:


tags.shape


# In[64]:


tags.isnull().any().any()


# In[65]:


tags=tags.dropna()


# In[66]:


tags.isnull().any().any()


# In[67]:


tags.shape


# In[68]:


get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(10,5))


# In[69]:


ratings.boxplot(column='rating', figsize=(10,5))


# In[70]:


tags['tag'].head()


# In[71]:


movies[['title','genres']].head()


# In[72]:


ratings[-10:]


# In[73]:


tag_counts = tags['tag'].value_counts()
tag_counts[-10:]


# In[74]:


tag_counts[:10].plot(kind='bar', figsize=(10,5))


# In[ ]:




