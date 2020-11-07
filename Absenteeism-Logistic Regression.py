#!/usr/bin/env python
# coding: utf-8

# ## Creating a Logistic Regreassion to Predict Absenteeism

# In[1]:


import pandas as pd
import numpy as np


# ## Load the Data

# In[2]:


data_preprocessed = pd.read_csv('Absenteeism_preprocessed.csv')


# In[3]:


data_preprocessed.head()


# ## Create the targets

# In[6]:


data_preprocessed['Absenteeism Time in Hours'].median()


# In[9]:


targets = np.where(data_preprocessed['Absenteeism Time in Hours']>
                   data_preprocessed['Absenteeism Time in Hours'].median(), 1,0)


# In[10]:


targets


# In[11]:


data_preprocessed['Extensive Absenteeism'] = targets


# In[12]:


data_preprocessed.head()


# In[15]:


targets.sum() / targets.shape[0]


# In[19]:


targets.shape[0]


# In[17]:


targets.sum() 


# In[20]:


data_with_targets = data_preprocessed.drop(['Absenteeism Time in Hours'], axis=1)


# In[21]:


data_with_targets


# In[ ]:




