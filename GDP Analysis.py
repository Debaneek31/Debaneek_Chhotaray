#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd


# In[45]:


ad = pd.read_csv(r'C:\Users\hp\Downloads\data.csv')


# In[46]:


ad


# In[47]:


ad.shape


# In[48]:


ad.columns


# In[49]:


ad.head()


# In[50]:


ad.tail()


# In[51]:


ad.isnull().sum()


# In[52]:


ad.describe() #it describe the data frame


# In[53]:


ad.describe().transpose() #it describe and reshape it


# In[54]:


ad.info()


# In[55]:


ad.columns


# In[56]:


df = ad


# In[57]:


df


# In[58]:


type(df)


# In[59]:


df.info()


# In[60]:


len(df.columns)


# In[61]:


df.head()


# In[62]:


df.tail()


# In[63]:


df.head(2)


# In[64]:


df.head(3)


# In[65]:


df.tail(2)


# In[66]:


df[::-1]


# In[67]:


df[:5]


# In[68]:


df[:6]


# In[69]:


df[6:]


# In[70]:


df[0:200:10]


# In[71]:


df.describe()


# In[72]:


df.describe().transpose()


# In[73]:


df.head(2)


# In[74]:


df.columns = ['a', 'b', 'c', 'd', 'e']


# In[75]:


df


# In[76]:


df.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
       'IncomeGroup']


# In[77]:


df


# In[78]:


df[:]


# In[79]:


df[:100]


# In[80]:


df[::10]


# In[81]:


df.columns


# In[82]:


df['CountryName']


# In[83]:


df[['CountryName','CountryCode']]


# In[84]:


df.dtypes


# In[85]:


df.columns 


# In[86]:


df.categorical = df [['CountryName', 'Country','Incomegroup']]
df_categorical.head()


# In[87]:


df.num = df [[]]


# In[88]:


df['IncomeGroup']


# In[89]:


df[['CountryName','BirthRate']]


# In[90]:


df[['CountryName','CountryCode']]


# In[91]:


df['BirthRate']


# In[92]:


df.columns


# In[93]:


cat = df [['BirthRate','IncomeGroup']]


# In[94]:


cat


# In[95]:


cat.columns


# In[96]:


cat =  df


# In[97]:


df[['CountryName', 'BirthRate']]


# In[98]:


df.head()


# In[99]:


df['myCalc'] = df.BirthRate * df.InternetUsers


# In[100]:


df.head(1)


# In[101]:


df


# In[102]:


df =  df.drop('myCalc', axis = 1)


# In[103]:


df


# In[104]:


df.head()


# In[105]:


df.InternetUsers


# In[106]:


df.InternetUsers<2 


# In[107]:


Filter = df.InternetUsers <2


# In[108]:


Filter


# In[109]:


df[Filter]


# In[110]:


df.BirthRate>40


# In[111]:


ulter = df.BirthRate>40


# In[112]:


ulter


# In[113]:


df[ulter]


# In[114]:


len(df[ulter])


# In[115]:


df[(df.InternetUsers > 40)& (df.InternetUsers<2)]


# In[116]:


df [(df.InternetUsers > 40)& (df.InternetUsers<2)]


# In[ ]:





# In[117]:


df [df.IncomeGroup == 'High income']


# In[118]:


df[df.IncomeGroup == 'Low income']


# In[119]:


df.IncomeGroup.unique()


# In[120]:


df.IncomeGroup.nunique()


# In[121]:


import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 6,2

import warnings
warnings.filterwarnings('ignore')


# In[122]:


df.head()


# In[123]:


df.InternetUsers


# In[124]:


vis1 = sns.distplot(df["InternetUsers"])


# In[125]:


vis2 = sns.displot(df["InternetUsers"])


# In[126]:


vis3 = sns.distplot(df["InternetUsers"], bins = 10)


# In[127]:


vis4 = sns.boxplot(data = df, x = "IncomeGroup", y= 'BirthRate')


# In[128]:


vis5 = sns.lmplot(data = df, x = "InternetUsers", y= 'BirthRate')


# In[129]:


vis6 = sns.lmplot(data = df, x = "InternetUsers", y= 'BirthRate', fit_reg= False)


# In[130]:


vis6 = sns.lmplot(data = df, x = "InternetUsers", y= 'BirthRate', fit_reg= True)


# In[131]:


vis8 = sns.lmplot(data = df, x = "InternetUsers", y= 'BirthRate', fit_reg= False, hue = 'IncomeGroup') 


# In[132]:


bin (35)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




