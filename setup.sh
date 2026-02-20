#!/bin/bash

# GitCommit AI Assistant - Professional Setup Script
# Developed by: Deepak Nemade (DN)
# Version: 2.0.0

echo "GitCommit AI Assistant - Professional Setup"
echo "Developed by: Deepak Nemade (DN)"
echo "Version: 2.0.0"
echo "============================================"

# Make main script executable
chmod +x main.py

echo "SUCCESS: Made main.py executable"

# Check Python version
python_version=$(python3 --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "SUCCESS: Python3 found - $python_version"
else
    echo "ERROR: Python3 not found. Please install Python 3.6+"
    exit 1
fi

# Check Git installation
git_version=$(git --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "SUCCESS: Git found - $git_version"
else
    echo "ERROR: Git not found. Please install Git"
    exit 1
fi

echo ""
echo "Setup completed successfully!"
echo ""
echo "Usage examples:"
echo "  python3 main.py           # Interactive mode"
echo "  python3 main.py --auto    # Auto-commit mode"  
echo "  python3 main.py --preview # Preview mode"
echo "  python3 main.py --sign    # GPG signed commit"
echo "  python3 main.py -s        # Signed-off commit"
echo ""
echo "Documentation: README.md"
echo "Professional Git workflow integration ready."
