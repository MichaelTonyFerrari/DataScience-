# Connect to our data
myRegressionData <- read.csv("C:/Users/Michael Ferraro/Desktop/Ex_Files_Data_Science_of_Marketing/Exercise_Files/03_02/regression-r.csv")

# Plot our data (broadcast & sales)
plot(myRegressionData$BROADCAST, myRegressionData$NET.SALES)
plot(myRegressionData$SOCIAL.MEDIA.VOLUM, myRegressionData$NET.SALES)
# Fit a line
myLM <- lm(myRegressionData$NET.SALES ~ myRegressionData$BROADCAST)
myLM2 <- lm(myRegressionData$NET.SALES ~ myRegressionData$SOCIAL.MEDIA.VOLUM)
# Visualize the line
lines(myRegressionData$BROADCAST, myLM$fitted)
linestwo(myRegressionData$SOCIAL.MEDIA.VOLUM, myLM2$fitted)

# Show our coefficients 
myLM$coefficients
myLM2$coefficients
