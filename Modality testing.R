#2025-02-07
#This script takes in a dataframe with one column of numeric data,
#assumed to be normally distributed.
#It determines the smallest number n, such that:
#if the data are bimodally distributed, the difference in means
#between the two groups is no bigger than n
#A unimodal data sample will lead to outputs close to 0
#Modality tests are performed using Hartigans' dip test

#Load dependencies
library(diptest)

#User-input variables (you should edit these!)
#A CSV file which can be loaded as a dataframe
csvDataPath <- ""
#The name of the column in the dataframe you want to study
cName <- ""
#The smallest conceivable difference of means (should probably be 0)
minDiff <- 0
#The largest conceivable difference of means
maxDiff <- 500
#The step size between minDiff and maxDiff you want to use
stepDiff <- 5
#The number of times you want to calculate Hartigans' dip test
iterations <- 10000

#Automatically calculated variables (you should not edit these!)
d <- read.csv(csvDataPath)
totalSamples <- nrow(d)
sample50 <- floor(totalSamples * 0.5)
sample90 <- floor(totalSamples * 0.9)
totalMean <- mean(d[[cName]])
totalSD <- sd(d[[cName]])
differences <- seq(minDiff, maxDiff, stepDiff)

hartigansD <- c()
meanD <- c()

#Simulated data
#Loop through each conceivable difference of means
for (difference in differences) {
  
  #This code can take time, so printing progress is useful
  print(difference)
 
  hartigansD <- c()
  
  #We simulate bimodal data with the difference of means being difference
  #(the data are sampled from a normal distribution, with the same
  #standard deviation as the real data)
  #We sample a random 90% of the simulated data
  #We calculate Hartigans' dip test, storing the result
  #We repeat all this iterations many times
  for (i in 1:iterations) {

    hartigansD <- append(
      hartigansD,
      as.numeric(dip.test(
        sample(
          c(
            rnorm(sample50, totalMean, totalSD),
            rnorm(sample50, totalMean - difference, totalSD)
          ),
          sample90)
        )[1]))
    
  }
  
  #The mean Hartigans' dip test statistic for the current difference of means
  meanD <- append(meanD, mean(hartigansD))
  
}

#A sort of look-up table:
#For each difference of means,
#it shows the expected Hartigans' dip test statistic
simMeanD <- data.frame(differences, meanD)

#Real data
hartigansD <- c()
meanD <- 0

#The process is the same as for the simulated data
#We sample 90% of the data randomly
#We calculate Hartigans' dip test statistic, storing the result
for (i in 1:iterations) {
  
  hartigansD <- append(
    hartigansD,
    as.numeric(dip.test(
      d[sample(totalSamples, sample90),][[cName]]
      )
      [1]))
  
}

#Mean Hartigans' dip test statistic for the real data
realMeanD <- mean(hartigansD)

#Calculate the smallest conceivable difference of means such that,
#if the real difference of means were any larger,
#then the real Hartigans' dip test statistic would reliably be larger too
output <- NA

for (i in seq_len(length(simMeanD$differences) - 1)) {
  
  subsetD <- simMeanD$meanD[i + 1:length(simMeanD$differences) - 1]
  
  if (all(realMeanD < subsetD, na.rm = TRUE)) {
    
    output <- simMeanD$differences[i]
    
    break
    
  }
  
}

#Print the output
print(paste("If d[[",
            cName,
            "]] is bimodally distributed, the difference between means of the two groups is no bigger than ",
            output, sep = ""))
