source("quiz.R")
library(rpart)

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=flowTrain)

# question 6
# Use print(model) to inspect your tree. Which populations, if any, is your tree incapable of recognizing? (Which populations do not appear on any branch?)
# (It's possible, but very unlikely, that an incorrect answer to this question is the result of improbable sampling.)
# Hint: Look
# pico
# nano
# ultra
# crypto (*)
# synecho
print(model)

# question 7
# Most trees will include a node near the root that applies a rule to the pe field, where particles with a value less than some threshold will descend down one branch, and particles with a value greater than some threshold will descend down a different branch.
# If you look at the plot you created previously, you can verify that the threshold used in the tree is evident visually.
# What is the value of the threshold on the pe field learned in your model?
# A: 5004

# question 8
# Based on your decision tree, which variables appear to be most important in predicting the class population?
# fsc_perp
# chl_small (*)
# fsc_big
# chl_big
# fsc_small
# pe (*)

# question 9
# How accurate was your decision tree on the test data? Enter a number between 0 and 1.
preds <- predict(model, flowTest, type="vector")
sum(preds == as.numeric(flowTest$pop))/nrow(flowTest)



# Random forests
library(randomForest)
modelRandomForest <- randomForest(fol, data=flowTrain)

# question 10
# What was the accuracy of your random forest model on the test data? Enter a number between 0 and 1.
predsRandomForest <- predict(modelRandomForest, flowTest)
sum(predsRandomForest == as.character(flowTest$pop))/nrow(flowTest)

# question 11
# After calling importance(model), you should be able to determine which variables appear to be most important in terms of the gini impurity measure. Which ones are they?
# chl_big (3)
# fsc_small (4)
# pe (1)
# chl_small (2)
# fsc_perp (5)
# fsc_big (6)

importance(modelRandomForest)



# supportVector
library(e1071)

modelSVM <- svm(fol, data=flowTrain)
# question 12
# What was the accuracy of your support vector machine model on the test data? Enter a number between 0 and 1.
predsSVM <- predict(modelSVM, flowTest)
sum(predsSVM == as.character(flowTest$pop))/nrow(flowTest)

# question 13
# Construct a confusion matrix for each of the three methods using the table function. What appears to be the most common error the models make?
# ultra is mistaken for nano
# ultra is mistaken for pico (*)
# nano is mistaken for ultra
# synecho is mistaken for pico
# pico is mistaken for ultra
# crypto is mistaken for ultra

table(pred = preds, true = flowTest$pop)
table(pred = predsRandomForest, true = flowTest$pop)
table(pred = predsSVM, true = flowTest$pop)


