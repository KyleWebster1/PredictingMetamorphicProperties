library("tidyverse")
scores <- read.csv("scores.csv")

# Format scores to be proper format
Types <- rep(c("Fit Time", 
           "Score Time", 
           "Precision", 
           "Recall", 
           "F1 Score", 
           "ROC_AUC"),2)
Score <- c(scores$Fit_Time[1], scores$Score_Time[1], scores$Precision[1], 
           scores$Recall[1], scores$F1[1], scores$ROC_AUC[1],
           scores$Fit_Time[2], scores$Score_Time[2], scores$Precision[2], 
           scores$Recall[2], scores$F1[2], scores$ROC_AUC[2])
Algo <- c(rep("SVM", 6), rep("NB", 6))
  
scores2 <- data.frame(Types, Score, Algo)
# Plot scores
ggplot(data = scores2, aes(x = Types, y = Score, fill = Algo)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric",
    y = "Average Score",
    x = "Metric Type"
  )