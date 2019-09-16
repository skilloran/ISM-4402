#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


bins = [0, 80, 100]
group_names = ['Fail', 'Pass']


# In[6]:


df['Pass or Fail'] = pd.cut(df['grade'], bins,
                           labels=group_names)
df


# In[7]:


pd.value_counts(df['Pass or Fail'])


# In[ ]:




