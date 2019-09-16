#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df = df.sort_values(by=['fname','lname','age','grade'],
                   ascending =[True, True, True, True])
df.head()


# In[ ]:




