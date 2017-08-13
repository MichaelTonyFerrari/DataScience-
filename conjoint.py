
# coding: utf-8

# In[5]:


# Load in our packages

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[6]:


# Connect to our data

myConjointData = pd.read_csv('C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/06_03/conjoint-py.csv')


# In[7]:


# See a snapshot of our data
myConjointData


# In[8]:


# Update the names of our vectors

names = {"Rank":"Rank", "P1": "PhotoF1","P2": "PhotoF2", "U1": "Ux1",          "U2": "Ux2", "D1":"SpecialSauce1",          "D2":"SpecialSauce2", "D3":"SpecialSauce3"        }


# Apply those new names
myConjointData.rename(columns = names, inplace=True)

# Confirm all is as we intended 
myConjointData.head(1)


# In[11]:


# Assign our test data to the x
X = myConjointData[['PhotoF1', 'PhotoF2', 'Ux1', 'Ux2', 'SpecialSauce1',                     'SpecialSauce2', 'SpecialSauce3']]
                 
# Assign a constant
X = sm.add_constant(X)

# Assign our resulting test data to the y
Y = myConjointData.Rank

# Perform a linear regression model 
myLinearRegression = sm.OLS(Y, X).fit()
myLinearRegression.summary()


# In[12]:


# Normalize values for each feature 
raw = [3.67,3.05,2.72]
norm = [float(i)/sum(raw) for i in raw]
norm


# In[13]:


# Graph our winning product features

labels = 'Special Sauce Feature Three', 'User Experience Feature One', 'Photo Feature One'
sizes = [39, 32, 29]
colors = ['yellowgreen', 'mediumpurple', 'lightskyblue'] 
explode = (0, 0.1, 0)    
plt.pie(sizes,              
        explode=explode,   
        labels=labels,      
        colors=colors,      
        autopct='%1.1f%%',  
        shadow=True,        
        startangle=70       
        )

plt.axis('equal')


# In[ ]:




