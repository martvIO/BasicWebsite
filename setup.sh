#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew is not installed. Please install Homebrew first."
    exit 1
fi

# Check if Python 3.12 is installed
if ! command -v python3.12 &> /dev/null
then
    echo "Python 3.12 is not installed. Installing Python 3.12..."
    brew install python@3.12
else
    echo "Python 3.12 is already installed."
fi

# Create the virtual environment
python3.12 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required modules from requirements.txt
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt file not found."
fi

echo "Setup complete!"
