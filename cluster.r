# Cluster Analysis 

# Connect to our case study data
clusterData <- read.csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/05_02/cluster-r.csv")

# Review our data
head(clusterData)
# Standardize the data
# scalling
datascaling <- scale(clusterData[-1])

# Run kmeans on our standardized data on 3 groups 
Groups <- kmeans(datascaling, 3)

# Load in our cluster library 
library(cluster)

# Visualize our clusters
clusplot.default(datascaling, Groups)

# Summarize our data
Groups$size
