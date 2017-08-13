# Connect to our data 
myConjointData <- read.csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/06_02/conjoint-r.csv")
myConjointDataProfilesMatrix <- read.csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/06_02/conjoint-r-profiles-matrix.csv")
myConjointDataLevelNames <- read.csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/06_02/conjoint-r-level-names.csv")

#install conjoint
install.packages("conjoint")

# Step 2.) Load the conjoint package
library(conjoint)
# Step 3 if needed.) If R throws an error, refer to the readme file in the Exercise_Files

# Model some of our data
caUtilities(y=myConjointData[1,], x=myConjointDataProfilesMatrix, z=myConjointDataLevelNames)

myConjointData[1,]
# Model all of our data
caUtilities(y=myConjointData, x=myConjointDataProfilesMatrix, z=myConjointDataLevelNames)





