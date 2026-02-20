#!/bin/bash

# GitCommit AI Assistant - Setup Script
# Developed by: Deepak Nemade (DN)

echo "🤖 GitCommit AI Assistant Setup"
echo "👨‍💻 Developed by: Deepak Nemade (DN)"
echo "=================================="

# Make main script executable
chmod +x main.py

echo "✅ Made main.py executable"

# Check Python version
python_version=$(python3 --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "✅ Python3 found: $python_version"
else
    echo "❌ Python3 not found. Please install Python 3.6+"
    exit 1
fi

# Check Git installation
git_version=$(git --version 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "✅ Git found: $git_version"
else
    echo "❌ Git not found. Please install Git"
    exit 1
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Usage examples:"
echo "  python3 main.py           # Interactive mode"
echo "  python3 main.py --auto    # Auto-commit mode"  
echo "  python3 main.py --preview # Preview mode"
echo ""
echo "📖 See README.md for detailed documentation"
