library(tidyverse)
library(dplyr)
library(plyr)
library(wesanderson)

raw_data <- read.csv("/Users/isaaclevy/Downloads/MSDS-Orientation-Computer-Survey(in).csv")

data <- raw_data[-c(1),]

accepted_os <- c("MacOS", "Windows 10", "Windows", "Any Linux", "All of the above")

data.clean <- subset(data, (data$CPU.Cycle.Rate..in.GHz. <= 10))

data.clean$Operating.System <- revalue(data.clean$Operating.System, c("Windows 10" = "Windows", "Any Linux" = "Other",
                                                     "All of the above" = "Other",
                                                     "Windows (by professional necessity), MacOS (by personal choice)" = "Other"))

data.clean %>%
  ggplot(aes(x = CPU.Cycle.Rate..in.GHz., fill = Operating.System)) +
  geom_histogram(binwidth = 0.5) +
  scale_x_continuous(name = "CPU Cycle Rate in GHz") +
  scale_y_discrete(name = "Count") + 
  scale_color_manual(values=wes_palette("GrandBudapest1", n=3)) +
  ggtitle("CPU Cycle Rate by Operating System")
