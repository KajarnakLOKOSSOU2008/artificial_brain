#!/bin/bash

# Clone the repository
git clone https://github.com/KajarnakLOKOSSOU2008/artificial_brain.git
cd artificial_brain

# Install Python dependencies
if command -v python3 &>/dev/null; then
    echo "Python is already installed"
else
    echo "Installing Python..."
    sudo apt-get install python3 -y
fi

if [ -f requirements.txt ]; then
    echo "Installing Python dependencies..."
    python3 -m pip install -r requirements.txt
else
    echo "No requirements.txt found for Python dependencies."
fi

# Install Node.js dependencies
if command -v node &>/dev/null; then
    echo "Node.js is already installed"
else
    echo "Installing Node.js..."
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

if [ -f package.json ]; then
    echo "Installing Node.js dependencies..."
    npm install
else
    echo "No package.json found for Node.js dependencies."
fi

echo "Installation complete. The project is ready for use!"