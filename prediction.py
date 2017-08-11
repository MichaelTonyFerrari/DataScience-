
# coding: utf-8

# In[17]:

# Establish the functionality for our assessment by bringing in the right packages
# Make sure to install these prior to mounting the packages 
# i.e. $ pip install pydotplus
# & visit http://www.graphviz.org/Download_macos.php

import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import pydotplus as pdot
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export
from sklearn.cross_validation import train_test_split

get_ipython().magic('matplotlib inline')


# In[5]:

# Connect to the data source
myPredictionData = pd.read_csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/04_03/prediction-py.csv")


# In[6]:

# Show column names for reference
myPredictionData.columns


# In[7]:

# Set up our cross validation function

feature_cols = ['capita', 'competition', 'weather', 'var1', 'var2', 'var3' ]

train_X, test_X,  train_y, test_y = train_test_split( myPredictionData[feature_cols],
                                    myPredictionData['sales_classification'])


# In[8]:

# Set up our depth list for our tree branches

depths_list = [2,3,4,5,6,7,8]

for depth in depths_list:
    clf_tree = DecisionTreeClassifier( max_depth = depth )
    clf_tree.fit( train_X, train_y )


# In[9]:

# Specify the number of branches for our tree
clf_tree = DecisionTreeClassifier(max_depth = 8)


# In[11]:

# Fit our training data to the x and to the y
clf_tree.fit(train_X, train_y)


# In[19]:

# Apply our test data to our model 
tree_predict = clf_tree.predict(test_X)


# In[20]:

# Visualize our tree
export_graphviz( clf_tree,
                out_file = "model_tree.odt",
                feature_names = train_X.columns )
model_tree_graph = pdot.graphviz.graph_from_dot_file( 'model_tree.odt' )
model_tree_graph.write_jpg( 'model_tree.jpg' )

from IPython.display import Image
Image(filename='model_tree.jpg')


# In[ ]:



