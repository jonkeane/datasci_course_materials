library(readr)
library(dplyr)
library(ggplot2)
library(caret)
flow <- read_csv("seaflow_21min.csv")
flow$pop <- as.factor(flow$pop)

# from http://www.gettinggeneticsdone.com/2011/02/split-data-frame-into-testing-and.html possibly better to use createDataPartition()?
splitdf <- function(dataframe, seed=NULL) {
  if (!is.null(seed)) set.seed(seed)
  index <- 1:nrow(dataframe)
  trainindex <- sample(index, trunc(length(index)/2))
  trainset <- dataframe[trainindex, ]
  testset <- dataframe[-trainindex, ]
  list(trainset=trainset,testset=testset)
}

split <- splitdf(flow)

flowTrain <- split$trainset
flowTest <- split$testset
