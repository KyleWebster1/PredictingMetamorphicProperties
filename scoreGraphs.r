library("tidyverse")
scores <- read.csv("scores.csv")

# Format scores to be proper format
algorithms <- c("Score Type", scores$Algorithm[1], scores$Algorithm[2])
fit <- c("Fit Time", scores$Fit_Time[1], scores$Fit_Time[2])
score <- c("Score Time", scores$Score_Time[1], scores$Score_Time[2])
precision <- c("Precision", scores$Precision[1], scores$Precision[2])
recall <- c("Recall", scores$Recall[1], scores$Recall[2])
f1 <- c("F1 Score", scores$F1[1], scores$F1[2])
auc <- c("ROC_AUC", scores$ROC_AUC[1], scores$ROC_AUC[2])

Types <- c("Fit Time", "Score Time", "Precision", "Recall", "F1 Score", "ROC_AUC")
SVM <- c(scores$Fit_Time[1], scores$Score_Time[1], scores$Precision[1], scores$Recall[1], scores$F1[1], scores$ROC_AUC[1])
NB <- c(scores$Fit_Time[2], scores$Score_Time[2], scores$Precision[2], scores$Recall[2], scores$F1[2], scores$ROC_AUC[2])

scores2 <- data.frame(Types, SVM, NB)
# Plot scores
ggplot(data = scores, aes(x = Types, y = SVM)) +
  geom_bar()