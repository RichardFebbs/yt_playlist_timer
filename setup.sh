#!/bin/bash

VENV_PATH="yt_timer_venv"
VENV_PIP="$VENV_PATH/bin/pip"

# Create the specified virtual environment if it doesn't exist
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH" || { echo "Failed to create a virtual environment."; exit 1; }
fi

# Check if the activation script exists
if [ ! -e "$VENV_PATH/bin/activate" ]; then
    echo "Virtual environment activation script not found"
    return 1 2>/dev/null || exit 1  # Don't kill shell if sourced
fi

# Install requirements if needed
packages="$($VENV_PIP freeze)" # Get the current environment package list
if [ -e requirements.txt ]; then
    # Use diff to compare the current packages with requirements.txt
    if [ -z $(diff <(echo "$packages") requirements.txt) ]; then
        echo "Setup complete"
    else
        $VENV_PIP install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
    fi
else
    echo -e "requirements.txt not found.\nSkipping Installation"
fi

echo -e "\n✅ Setup complete!"
echo "👉 To activate the virtual environment, run:"
echo "   source $VENV_PATH/bin/activate"
