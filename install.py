#!/usr/bin/env python3
"""
GitCommit AI Assistant - Auto-Install Script
Installs Git hooks for automatic commit message generation
Developed by: Deepak Nemade (DN)
"""

import os
import sys
import subprocess
from pathlib import Path

def check_git_repo():
    """Check if in git repository"""
    try:
        subprocess.run(['git', 'rev-parse', '--git-dir'], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_git_hooks_dir():
    """Get git hooks directory"""
    try:
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                              capture_output=True, text=True, check=True)
        return Path(result.stdout.strip()) / 'hooks'
    except subprocess.CalledProcessError:
        return None

def install_prepare_commit_msg_hook(app_path, hooks_dir):
    """Install prepare-commit-msg hook"""
    hook_path = hooks_dir / 'prepare-commit-msg'
    
    hook_content = f'''#!/bin/bash
# GitCommit AI Assistant - Auto Hook
# Developed by: Deepak Nemade (DN)

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2

# Only run for regular commits (not merge, squash, etc.)
if [ -z "$COMMIT_SOURCE" ] || [ "$COMMIT_SOURCE" = "message" ]; then
    # Check if there are staged changes
    if git diff --cached --quiet; then
        exit 0
    fi
    
    # Generate commit message using AI Assistant
    python3 "{app_path}/main.py" --hook "$COMMIT_MSG_FILE"
fi
'''
    
    with open(hook_path, 'w') as f:
        f.write(hook_content)
    
    # Make executable
    os.chmod(hook_path, 0o755)
    return True

def add_hook_mode_to_main():
    """Add hook mode to main.py"""
    main_path = Path(__file__).parent / 'main.py'
    
    # Read current content
    with open(main_path, 'r') as f:
        content = f.read()
    
    # Add hook mode if not exists
    if '--hook' not in content:
        # Add hook argument to parser
        parser_section = '''    parser.add_argument('-s', '--signoff', action='store_true',
                       help='Add signed-off-by line (equivalent to git commit -s)')
    parser.add_argument('--version', action='version', version='GitCommit AI Assistant 2.0.0')'''
        
        new_parser_section = '''    parser.add_argument('-s', '--signoff', action='store_true',
                       help='Add signed-off-by line (equivalent to git commit -s)')
    parser.add_argument('--hook', metavar='FILE',
                       help='Hook mode: write message to file (internal use)')
    parser.add_argument('--version', action='version', version='GitCommit AI Assistant 2.0.0')'''
        
        content = content.replace(parser_section, new_parser_section)
        
        # Add hook handling to main function
        main_call = '''    try:
        app = GitCommitAI()
        app.run(auto_commit=args.auto, preview_only=args.preview, 
                sign=args.sign, signoff=args.signoff)'''
        
        new_main_call = '''    try:
        app = GitCommitAI()
        if args.hook:
            app.run_hook_mode(args.hook)
        else:
            app.run(auto_commit=args.auto, preview_only=args.preview, 
                    sign=args.sign, signoff=args.signoff)'''
        
        content = content.replace(main_call, new_main_call)
        
        # Add hook mode method to class
        class_end = '''        return commit_message + body
    
    def commit_changes(self, message: str, sign: bool = False, signoff: bool = False) -> bool:'''
        
        hook_method = '''        return commit_message + body
    
    def run_hook_mode(self, commit_file: str):
        """Hook mode: generate message and write to commit file"""
        # Get staged changes
        diff_content = self.get_staged_changes()
        if not diff_content or not diff_content.strip():
            return
        
        # Get staged files and analyze
        staged_files = self.get_staged_files()
        analysis = self.analyze_changes(diff_content, staged_files)
        
        # Generate message
        commit_message = self.generate_commit_message(analysis, diff_content)
        
        # Write to commit file
        with open(commit_file, 'w') as f:
            f.write(commit_message)
    
    def commit_changes(self, message: str, sign: bool = False, signoff: bool = False) -> bool:'''
        
        content = content.replace(class_end, hook_method)
        
        # Write updated content
        with open(main_path, 'w') as f:
            f.write(content)

def main():
    print("GitCommit AI Assistant - Auto-Install")
    print("Developed by: Deepak Nemade (DN)")
    print("===================================")
    
    if not check_git_repo():
        print("ERROR: Not in a git repository")
        sys.exit(1)
    
    hooks_dir = get_git_hooks_dir()
    if not hooks_dir:
        print("ERROR: Could not find git hooks directory")
        sys.exit(1)
    
    app_path = Path(__file__).parent.absolute()
    
    print(f"Installing hooks in: {hooks_dir}")
    
    # Create hooks directory if not exists
    hooks_dir.mkdir(exist_ok=True)
    
    # Add hook mode to main.py
    print("Adding hook mode to main.py...")
    add_hook_mode_to_main()
    
    # Install prepare-commit-msg hook
    print("Installing prepare-commit-msg hook...")
    install_prepare_commit_msg_hook(app_path, hooks_dir)
    
    print("")
    print("SUCCESS: GitCommit AI Assistant installed!")
    print("")
    print("Auto-detection enabled:")
    print("- Automatic commit message generation on 'git commit'")
    print("- No need to run main.py manually")
    print("- Works with all git commit options (-S, -s, etc.)")
    print("")
    print("To uninstall: rm .git/hooks/prepare-commit-msg")

if __name__ == "__main__":
    main()
