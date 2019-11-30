library("tidyverse")
## Add functions
addScores <- read.csv("addMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/addFunc.png", width = 614, height = 314)

# Plot scores
ggplot(data = addScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for ADD Functions",
    y = "Average Score",
    x = "Metric Type"
  )
dev.off()

## Exc functions
excScores <- read.csv("excMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/excFunc.png", width = 614, height = 314)

# Plot scores
ggplot(data = excScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for EXC Functions",
    y = "Average Score",
    x = "Metric Type"
  )

dev.off()

## Inc functions
incScores <- read.csv("incMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/incFunc.png", width = 614, height = 314)
# Plot scores
ggplot(data = incScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for INC Functions",
    y = "Average Score",
    x = "Metric Type"
  )
dev.off()

## Inv functions
invScores <- read.csv("invMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/invFunc.png", width = 614, height = 314)
# Plot scores
ggplot(data = invScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for INV Functions",
    y = "Average Score",
    x = "Metric Type"
  )
dev.off()

## Mul functions
mulScores <- read.csv("mulMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/mulFunc.png", width = 614, height = 314)
# Plot scores
ggplot(data = mulScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for MUL Functions",
    y = "Average Score",
    x = "Metric Type"
  )
dev.off()

# Per Functions
perScores <- read.csv("perMetrics.csv") %>%
  filter(
    Type != c('fit_time', 'score_time')
  )

png("graphs/perFunc.png", width = 614, height = 314)
# Plot scores
ggplot(data = perScores, aes(x = Type, y = Score, fill = Algorithm)) +
  geom_col(width = 0.5, position = "dodge") +
  labs(
    title = "Average Score of NB and SVM by Metric for PER Functions",
    y = "Average Score",
    x = "Metric Type"
  )
dev.off()