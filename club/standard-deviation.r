# Check if ggplot2 is installed
if (!require("ggplot2", quietly = TRUE)) {
    print("ggplot2 not found. Installing...")
    install.packages("ggplot2", repos = "http://cran.us.r-project.org")
} else {
    print("ggplot2 is already installed")
}

# Verify installation
if (require("ggplot2", quietly = TRUE)) {
    print("ggplot2 installation verified!")
    print(paste("Version:", packageVersion("ggplot2")))
} else {
    print("Error: ggplot2 installation failed")
} 
# Load required library
library(ggplot2)

# Create data frame for the standard normal curve
x <- seq(-5, 5, length.out = 1000)
y <- dnorm(x)
df <- data.frame(x = x, y = y)

# Calculate sigma points for annotations
car_sigma <- qnorm(1/366)
lightning_sigma <- qnorm(1/500000)
plane_sigma <- qnorm(1/11000000)

# Create the plot
p <- ggplot(df, aes(x = x, y = y)) +
  # Add the normal curve
  geom_line(size = 1) +
  
  # Add filled regions for sigma intervals
  geom_area(data = subset(df, x >= -1 & x <= 1), 
            fill = "red", alpha = 0.2) +
  geom_area(data = subset(df, x >= -2 & x <= 2), 
            fill = "yellow", alpha = 0.1) +
  geom_area(data = subset(df, x >= -3 & x <= 3), 
            fill = "green", alpha = 0.1) +
  
  # Add vertical lines for sigma values
  geom_vline(xintercept = -3:3, linetype = "dashed", 
             color = "gray", alpha = 0.5) +
  
  # Add sigma labels
  geom_text(data = data.frame(x = -3:3, y = rep(-0.02, 7)),
            aes(x = x, y = y, label = paste0(x, "σ")),
            size = 4) +
  
  # Add annotations for real-world probabilities
  annotate("text", x = car_sigma + 2, y = 0.3,
           label = paste0("🚗 Car accident (1 in 366)\n", 
                         round(car_sigma, 2), "σ"),
           fontface = "bold", size = 4) +
  annotate("text", x = lightning_sigma + 2.5, y = 0.2,
           label = paste0("⚡ Lightning strike (1 in 500k)\n",
                         round(lightning_sigma, 2), "σ"),
           fontface = "bold", size = 4) +
  annotate("text", x = plane_sigma + 3, y = 0.1,
           label = paste0("✈️ Plane accident (1 in 11M)\n",
                         round(plane_sigma, 2), "σ"),
           fontface = "bold", size = 4) +
  
  # Add arrows connecting annotations to points
  geom_segment(aes(x = car_sigma + 2, y = 0.3,
                   xend = car_sigma, yend = dnorm(car_sigma)),
               arrow = arrow(length = unit(0.2, "cm"))) +
  geom_segment(aes(x = lightning_sigma + 2.5, y = 0.2,
                   xend = lightning_sigma, yend = dnorm(lightning_sigma)),
               arrow = arrow(length = unit(0.2, "cm"))) +
  geom_segment(aes(x = plane_sigma + 3, y = 0.1,
                   xend = plane_sigma, yend = dnorm(plane_sigma)),
               arrow = arrow(length = unit(0.2, "cm"))) +
  
  # Add probability text box
  annotate("text", x = 3.5, y = 0.35,
           label = paste("Probabilities:",
                        "±1σ: 68.27%",
                        "±2σ: 95.45%",
                        "±3σ: 99.73%",
                        "±4σ: 99.994%",
                        "±5σ: 99.99994%",
                        sep = "\n"),
           hjust = 0, vjust = 1,
           box.padding = unit(0.5, "lines"),
           size = 4) +
  
  # Customize the plot
  labs(title = "Standard Normal Distribution with Annual Risk Comparisons",
       x = "Standard Deviations (σ)",
       y = "Probability Density") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14),
        axis.title = element_text(size = 12))

# Display the plot
print(p)

# Optionally save the plot
# ggsave("standard_normal.pdf", p, width = 12, height = 6) 