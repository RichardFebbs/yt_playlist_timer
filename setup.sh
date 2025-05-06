#!/bin/bash

VENV_PATH="./yt_timer_venv"

# Create the specified virtual environment if it doesn't exist
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"
fi

# Check if the activation script exists
if [ -e "$VENV_PATH"/scripts/activate ]; then
    # Start the environment if it exists
    source env/bin/activate
else
    echo "Virtual environment activation script not found"
    exit 1
fi

# Install requirements if the file exists
if [ -e requirements.txt]; then
    pip install -r requirements.txt
else
    echo -e "requirements.txt not found.\nSkipping Installation"
fi
