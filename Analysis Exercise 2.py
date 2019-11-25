#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:





# In[ ]:





# In[4]:


df['Cars Sold'].mean()


# In[5]:


df['Cars Sold'].max()


# In[6]:


df['Cars Sold'].min()


# In[7]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[8]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[9]:


df['Years Experience'].mean()


# In[10]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[11]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


import matplotlib.pyplot as plt
import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.columns = ['FirstName', 'LastName', 'Gender', 'HoursWorked', 'SalesTraining', 'YearsExperience', 'CarsSold']
df['CarsSold'].mean()
df['HoursWorked'].mean()
HoursSold= zip(Lname, HoursWorked, CarsSold)
df = pd.DataFrame(data= HoursSold,
                 columns=['Last Name', 'Avg. Hours Worked', 'Avg. Cars Sold'])
df2= df.set_index(df['Last Name'])
get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')
df2.plot(kind="bar")





# In[72]:


import pandas as pd
import matplotlib.pyplot as plt
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.columns = ['FirstName', 'LastName', 'Gender', 'HoursWorked', 'SalesTraining', 'YearsExperience', 'CarsSold']
Exper= zip(Lname,'Years Experience',CarsSold)
df = pd.DataFrame(data = Exper,
                 columns =['Last Name', 'Years of Experience', 'Cars Sold'])
df2=df.set_index(df['Last Name'])
get_ipython().magic(u'matplotlib inline')
df.plot()
df2.plot()


# In[36]:





# In[ ]:




