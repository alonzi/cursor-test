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