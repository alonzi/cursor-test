#!/bin/bash

echo "Starting R installation script..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install R
echo "Installing R..."
brew install r

# Verify R installation
echo "Verifying R installation..."
R --version

# Install required R package (ggplot2)
echo "Installing ggplot2 package..."
R -e "install.packages('ggplot2', repos='http://cran.us.r-project.org')"

echo "Installation complete! You can now run your R scripts."
echo "To run the standard deviation plot, use:"
echo "Rscript standard-deviation.r" 