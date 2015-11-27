source("quiz.R")

# question 15
# The variables in the dataset were assumed to be continuous, but one of them takes on only a few discrete values, suggesting a problem. Which variable exhibits this problem?
# pe
# fsc_big (*)
# fsc_small
# chl_small
# fsc_perp
# chl_big

ggplot(flow) + aes(x=fsc_small) +geom_histogram()
ggplot(flow) + aes(x=fsc_perp) +geom_histogram()
ggplot(flow) + aes(x=fsc_big) +geom_histogram()
ggplot(flow) + aes(x=pe) +geom_histogram()
ggplot(flow) + aes(x=chl_small) +geom_histogram()
ggplot(flow) + aes(x=chl_big) +geom_histogram()

# question 14
# After removing data associated with file_id 208, what was the effect on the accuracy of your svm model? Enter a positive or negative number representing the net change in accuracy, where a positive number represents an improvement in accuracy and a negative number represents a decrease in accuracy.
ggplot(flow) + aes(y=chl_big, x=time) +geom_point(alpha=0.1)
ggplot(filter(flow, file_id != 208)) + aes(y=chl_big, x=time) +geom_point(alpha=0.1)
# can't find the band?

splitSub <- splitdf(filter(flow, file_id != 208))

flowTrainSub <- splitSub$trainset
flowTestSub <- splitSub$testset

modelSVMSub <- svm(fol, data=flowTrainSub)
# question 12
# What was the accuracy of your support vector machine model on the test data? Enter a number between 0 and 1.
predsSVMSub <- predict(modelSVMSub, flowTestSub)
sum(predsSVMSub == as.character(flowTestSub$pop))/nrow(flowTestSub) - sum(predsSVM == as.character(flowTest$pop))/nrow(flowTest)


