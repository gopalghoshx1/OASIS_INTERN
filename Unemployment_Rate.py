#!/usr/bin/env python
# coding: utf-8

# # Surjo Gopal Ghosh

# # Importing libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px


# # Reading the Unemployment CSV file 

# In[2]:


df= pd.read_csv('Downloads/Unemployment_Rate_upto_11_2020.csv')


# # Displaying Data

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.rename(columns={'Region': 'State',
                    ' Estimated Unemployment Rate (%)' : 'Estimated Unemployment Rate',
                    ' Estimated Labour Participation Rate (%)': 'Estimated Labour Participation Rate',
                    'Region.1' : 'Region'}, inplace=True)


# In[8]:


df.columns


# In[9]:


df


# In[10]:


df.info()


# # Searching Null Values

# In[11]:


df.isnull().sum()


# In[12]:


df.shape


# In[13]:


df[' Date'] = pd.to_datetime(df[' Date']).dt.strftime('%B')


# In[14]:


df.info()


# In[15]:


df[' Date'].value_counts(normalize= True)*100


# 
# # Analyze and Visualization

# In[16]:


plt.figure(figsize=(12,9))
sns.barplot( x=' Date', y='Estimated Unemployment Rate', data =df )
plt.title('Estimated Unemployment Rate In Each Month',size= 20)
plt.xlabel('Month of 2020',size =15)
plt.ylabel('Estimated Unemployment Rate',size =15)
plt.show()


# In[17]:


plt.figure(figsize=(12,9))
sns.barplot( x=' Date', y='Estimated Labour Participation Rate', data =df )
plt.title('Estimated Labour Participation Rate In Each Month',size= 20)
plt.xlabel('Month of 2020', size =15)
plt.ylabel('Estimated Labour Participation Rate', size =15)
plt.show()


# In[18]:


plt.figure(figsize=(12,9))
sns.heatmap(df.corr())


# In[19]:


plt.figure(figsize=(12,9))
sns.histplot(x=' Estimated Employed', data =df , hue = 'Region')
plt.title('Employee From The Regions  ',size= 20)
plt.xlabel(' Estimated Employed', size =15)
plt.ylabel('Number of Employe', size =15)
plt.show()


# In[20]:


plt.figure(figsize=(12,9))
sns.histplot(x='Estimated Unemployment Rate', data =df , hue = 'Region')
plt.title('Unemployment Rate In Regions  ',size= 20)
plt.xlabel('Estimated Unemployment Rate', size =15)
plt.ylabel('Number of Employe', size =15)
plt.show()


# In[21]:


plt.figure(figsize=(9,6))
sns.scatterplot(x= 'longitude',y= 'latitude', data = df, hue = 'Region',s=200)
plt.title('longitude and latitude Of Every Region',size= 20)
plt.xlabel('longitude' , size= 15)
plt.ylabel('latitude', size= 15)
plt.show()


# In[22]:


plt.figure(figsize=(15,9))
sns.barplot(x= 'State' ,y= ' Estimated Employed', data= df)
plt.xticks(rotation= 90)
plt.title('Estimated Employee In Every State',size= 20)
plt.xlabel('State' , size= 15)
plt.ylabel('Estimated Employee', size= 15)
plt.show()


# In[30]:


uneployed= df[['State', 'Region', 'Estimated Unemployment Rate']]
px.sunburst(uneployed, path=[ 'Region','State'],
           values='Estimated Unemployment Rate',
           height=700,width=700, color_continuous_scale='RdY1Gn',
           title= 'Unemployed Rate In India')


# # Thank You
