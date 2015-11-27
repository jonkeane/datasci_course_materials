source("quiz.R")

# question 5
# In the plot of pe vs. chl_small, the particles labeled ultra should appear to be somewhat "mixed" with two other populations of particles. Which two populations?
# pico (*)
# crypto
# nano (*)
# synecho

ggplot(flow) +aes(y=pe, x=chl_small, color=pop) + geom_point()
