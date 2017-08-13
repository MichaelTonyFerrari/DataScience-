
# coding: utf-8

# In[1]:


# Load in our packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans

get_ipython().magic('matplotlib inline')


# In[2]:


# Connect to our case study data set

myClusterData = pd.read_csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/05_03/cluster-py.csv")


# In[5]:


# Have a look at our data
myClusterData.head(3)


# In[7]:


# Plot our b1 & b3 data
plt.scatter(myClusterData.b1,  myClusterData.b3)
plt.show()


# In[8]:


# Assign values to x & y 

x = [16, 25, 18, 22, 5, 10, 21, 4, 30, 25]
y = [11, 7, 9, 16, 16, 15, 16, 7, 17, 5]


# In[9]:


# Plot our x & y values
plt.scatter(x,y)


# In[10]:


# Pivot our data to work as an array 
X = np.array([[16, 11],
              [25, 7],
              [18, 9],
              [22, 16],
              [5, 16],
              [10, 15],
              [21, 16],
              [4, 7],
              [30, 17],
              [25, 5]])


# In[12]:


# Assign the value of n clusters / run the algorithm / assign centroids / label our group names 

Groups = KMeans(n_clusters=3)

Groups.fit(X)

centroids = Groups.cluster_centers_

labels = Groups.labels_


# In[13]:


# Set up our color palette

colors = ["b.","g.","r.","c.","m."]

# Plot each point

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

# Generate the view

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5)
plt.show()


# In[ ]:




