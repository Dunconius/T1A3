#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    echo "Python is not installed. Installing..."
    
    # Install Python using the package manager (apt in this case)
    sudo apt update
    sudo apt install -y python3
    
    # Check if the installation was successful
    if command -v python3 &>/dev/null; then
        echo "Python installed successfully."
    else
        echo "Failed to install Python. Please install it manually."
        exit 1
    fi
fi

VENV_DIR=".venv"

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment $VENV_DIR already exists."
else
    echo "Virtual environment $VENV_DIR does not exist. Creating..."

    # Create the virtual environment
    python3 -m venv "$VENV_DIR"

    # Check if the virtual environment creation was successful
    if [ -d "$VENV_DIR" ]; then
        echo "Virtual environment $VENV_DIR created successfully."
    else
        echo "Failed to create virtual environment. Please check and try again."
        exit 1
    fi
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

pip3 install colored
pip3 install pandas
python3 main.py