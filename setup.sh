#!/bin/bash

# GitCommit AI Assistant - Setup Script
# Developed by: Deepak Nemade (DN)

echo "GitCommit AI Assistant - Setup"
echo "Developed by: Deepak Nemade (DN)"
echo "=============================="

chmod +x main.py
echo "SUCCESS: Made main.py executable"

python_version=$(python3 --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "SUCCESS: $python_version"
else
    echo "ERROR: Python3 not found"
    exit 1
fi

git_version=$(git --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "SUCCESS: $git_version"
else
    echo "ERROR: Git not found"
    exit 1
fi

echo ""
echo "Setup completed successfully!"
echo "Usage: python3 main.py --help"
