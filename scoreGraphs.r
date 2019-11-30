library("tidyverse")
scores <- read.csv("addMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

# Plot scores
ggplot(data = scores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric",
    y = "Average Score",
    x = "Metric Type"
  )