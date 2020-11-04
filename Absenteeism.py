#!/usr/bin/env python
# coding: utf-8

# In[243]:


import pandas as pd
import numpy as np

#import libraries for plots
import matplotlib.pyplot as plt
import seaborn as sns


# In[244]:


# reading the data file
df = pd.read_csv('Absenteeism_data.csv')


# In[245]:


# First 5 rows of data
df.head()


# ## Analyze the Reason for Absence column
# 

# In[246]:


df["Reason for Absence"].min()


# In[247]:


df["Reason for Absence"].max()


# In[248]:


pd.unique(df["Reason for Absence"])


# In[255]:


#looking for the unique values of the column
df["Reason for Absence"].unique()


# In[250]:


len(df["Reason for Absence"].unique())


# In[256]:


# ordered the unique value to find any missing values and number 20 is missing
sorted(df["Reason for Absence"].unique())


# In[257]:


# get age_dummies 
reasons_col = pd.get_dummies(df["Reason for Absence"].unique())


# In[258]:


reasons_col


# In[264]:


#add a checck column to identify the sum of the age_dummies
reasons_col['check'] = reasons_col.sum(axis=1)


# In[265]:


reasons_col


# In[266]:


reasons_col['check'].unique()


# In[269]:


reasons_col = reasons_col.drop(['check'], axis=1)


# In[270]:


reasons_col


# ## .get_dummies()

# In[271]:


age_dummies = pd.get_dummies(df['Age'].unique())
age_dummies


# In[272]:


age_dummies['check'] = age_dummies.sum(axis=1)


# In[273]:


age_dummies


# In[274]:


age_dummies=age_dummies.drop(['check'], axis=1)
age_dummies.head()


# In[275]:


reasons_columns = pd.get_dummies(df["Reason for Absence"], drop_first = True)


# In[276]:


reasons_col


# ## Group the reason for Absence

# In[277]:


df.columns.values


# In[278]:


reasons_col.columns.values


# In[279]:


df = df.drop(['ID','Reason for Absence'],axis = 1)


# In[280]:


df


# In[398]:


reasons_col.loc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14]].max(axis=1)


# In[399]:


reason_type1 =reasons_col.loc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14]].max(axis=1)
reason_type2 =reasons_col.iloc[:,[ 15,16,17]].max(axis=1)
reason_type3 =reasons_col.iloc[:, [18,19,20,21]].max(axis=1)
reason_type4 =reasons_col.iloc[:, [22]].max(axis=1)


# In[350]:


reason_type1


# ## Concatenate Column Values

# In[351]:


df.head()


# In[352]:


df = pd.concat([df,reason_type1, reason_type2, reason_type3, reason_type4 ], axis=1)
df.head()


# In[353]:


df.columns.values


# In[354]:


col_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']


# In[396]:


df.columns =  col_names
df.head()


# ## Reorder Columns

# In[356]:


column_names_reoder = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[357]:


df = df [column_names_reoder]


# In[395]:


df.head()


# ## Create a checkpoint 

# In[359]:


df_reason_mod = df.copy()


# In[360]:


df_reason_mod.head(7)


# ## Date

# In[361]:


type(df_reason_mod['Date'][0])


# In[362]:


df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'])
 


# In[363]:


df_reason_mod['Date']


# In[364]:


df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format='%d %m %Y')


# In[365]:


df_reason_mod['Date']


# In[366]:


type(df_reason_mod['Date'])


# In[367]:


df_reason_mod.info()


# In[368]:


df_reason_mod
df_reason_mod.head()


# ## Extract the Month Value:

# In[369]:


df_reason_mod['Date'][0]


# In[370]:


df_reason_mod['Date'][0].month


# In[371]:


list_months = []
list_months


# In[372]:


for i in range (700):
    list_months.append(df_reason_mod['Date'][i].month)


# In[373]:


list_months


# In[374]:


len(list_months)


# In[375]:


df_reason_mod['Month Value']=list_months
df_reason_mod.head()


# ## Extract the Date of the Week:

# In[376]:


df_reason_mod['Date'][699].weekday()


# In[377]:


df_reason_mod['Date'][699]


# In[378]:


def date_to_weekday (date_value):
    return date_value.weekday()


# In[379]:


df_reason_mod ['Date of the Week'] = df_reason_mod['Date'].apply(date_to_weekday)


# In[380]:


df_reason_mod.head()


# ### Transportation Expense, Distance to Work, Age, Daily Work Load Average, Body Mass Index

# In[381]:


type(df_reason_mod['Transportation Expense'][0])


# In[382]:


type(df_reason_mod['Distance to Work'][0])


# In[383]:


type(df_reason_mod['Age'][0])


# In[384]:


type(df_reason_mod['Daily Work Load Average'][0])


# In[385]:


type(df_reason_mod['Body Mass Index'][0])


# ## Education, Children, Pets

# In[386]:


df_reason_mod['Education'].unique()


# In[387]:


df_reason_mod['Education'].value_counts()


# In[388]:


df_reason_mod['Education'] = df_reason_mod['Education'].map({1:0, 2:1, 3:1, 4:1})


# In[389]:


df_reason_mod['Education'].unique()


# In[390]:


df_reason_mod['Education'].value_counts()


# ## Final Chekpoint

# In[391]:


df_preprocessed = df_reason_mod.copy()
df_preprocessed.head(5)


# In[392]:


df_preprocessed.to_csv('Absenteeism_preprocessed.csv', index=False)
df_preprocessed


# In[ ]:





# In[ ]:




