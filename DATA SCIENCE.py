#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#Initialize list of lists
data = [['Ayo', 10], ['Imran, 15'], ['Chucks', 14]]

#Create the prompts DataFrame from the list and adding column headers
df= pd.DataFrame(data, columns = ['Name', 'age' ])

#Print dataframe
df


# In[2]:


#create the pandas DataFrame from the dictionary of array list
#Example 1:
data = {'Name' : ['Ayo', 'Imran', 'Chucks'], 'Age':[10, 15, 14]}

#create the pandas Dataframe from the list and adding column headers
data=pd.DataFrame(data)

#print dataframe
df


# In[3]:


#Example 2:
#Population and area (km/square) of some states in Nigeria and their capital

dict_data = {"State": ["Abia", "Adamawa", "Lagos","Osun", "Rivers","Akwa-Ibom" ], "Capital": ["Umuahia", "Yola", "Ikeja", "Osogbo", "Portharcourt", "Uyo"], "Area": [6320, 36917, 3345, 9251, 11077, 11223], "Population": [2845380, 3178950, 9113605, 3416959, 5198605,2334453]}

df= pd.DataFrame(dict_data)

df


# In[7]:


csv_df = pd.read_csv('data.csv')
csv_df


# In[8]:


#To show the features in the dataset
csv_df .columns


# In[ ]:




