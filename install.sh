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


# Check if the virtual environment directory exists
VENV_DIR=".venv"

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

# Check if Pandas is installed
if python3 -c "import pandas" &>/dev/null; then
    echo "Pandas is already installed."
else
    echo "Pandas is not installed. Installing..."

    # Install Pandas using pip
    python3 -m pip install pandas

    # Check if the installation was successful
    if python3 -c "import pandas" &>/dev/null; then
        echo "Pandas installed successfully."
    else
        echo "Failed to install Pandas. Please check and try again."
        exit 1
    fi
fi

# Check if Pandas is installed
if python3 -c "import colored" &>/dev/null; then
    echo "Colored is already installed."
else
    echo "Colored is not installed. Installing..."

    # Install Pandas using pip
    python3 -m pip install colored

    # Check if the installation was successful
    if python3 -c "import colored" &>/dev/null; then
        echo "Colored installed successfully."
    else
        echo "Failed to install Colored. Please check and try again."
        exit 1
    fi
fi

python3 main.py