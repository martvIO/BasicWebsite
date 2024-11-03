#!/bin/bash

# Check if the .venv directory exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment .venv not found. Please create it first."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Run the application
python app.py

# Deactivate the environment after the app is closed
deactivate
