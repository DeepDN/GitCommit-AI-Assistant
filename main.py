#!/usr/bin/env python3
"""
GitCommit AI Assistant
A local application that reads staged Git changes and uses a local AI model 
to generate intelligent commit message summaries.

Developed by: Deepak Nemade (DN)
Version: 1.0.0
"""

import subprocess
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GitCommitAI:
    """Main class for Git Commit AI Assistant"""
    
    def __init__(self):
        self.app_name = "GitCommit AI Assistant"
        self.version = "1.0.0"
        self.developer = "Deepak Nemade (DN)"
        
    def check_git_repo(self) -> bool:
        """Check if current directory is a git repository"""
        try:
            subprocess.run(['git', 'rev-parse', '--git-dir'], 
                         check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def get_staged_changes(self) -> Optional[str]:
        """Get staged changes from git"""
        try:
            result = subprocess.run(['git', 'diff', '--cached'], 
                                  capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Error getting staged changes: {e}")
            return None
    
    def get_staged_files(self) -> List[str]:
        """Get list of staged files"""
        try:
            result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                                  capture_output=True, text=True, check=True)
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except subprocess.CalledProcessError:
            return []
    
    def analyze_changes(self, diff_content: str, files: List[str]) -> Dict[str, any]:
        """Analyze the changes to understand the context"""
        analysis = {
            'files_changed': len(files),
            'file_types': set(),
            'change_type': 'update',
            'lines_added': 0,
            'lines_removed': 0,
            'files': files
        }
        
        # Analyze file types
        for file in files:
            if '.' in file:
                ext = file.split('.')[-1].lower()
                analysis['file_types'].add(ext)
        
        # Count additions and deletions
        for line in diff_content.split('\n'):
            if line.startswith('+') and not line.startswith('+++'):
                analysis['lines_added'] += 1
            elif line.startswith('-') and not line.startswith('---'):
                analysis['lines_removed'] += 1
        
        # Determine change type
        if analysis['lines_removed'] == 0:
            analysis['change_type'] = 'add'
        elif analysis['lines_added'] == 0:
            analysis['change_type'] = 'remove'
        elif analysis['lines_added'] > analysis['lines_removed'] * 2:
            analysis['change_type'] = 'feature'
        elif analysis['lines_removed'] > analysis['lines_added'] * 2:
            analysis['change_type'] = 'refactor'
        
        return analysis
    
    def generate_commit_message(self, analysis: Dict[str, any], diff_content: str) -> str:
        """Generate commit message using local AI logic (rule-based for privacy)"""
        
        # Determine commit type based on analysis
        commit_types = {
            'add': 'feat',
            'feature': 'feat',
            'remove': 'refactor',
            'refactor': 'refactor',
            'update': 'chore'
        }
        
        commit_type = commit_types.get(analysis['change_type'], 'chore')
        
        # Generate scope based on file types
        file_types = list(analysis['file_types'])
        if 'py' in file_types:
            scope = 'python'
        elif 'js' in file_types or 'ts' in file_types:
            scope = 'frontend'
        elif 'md' in file_types:
            scope = 'docs'
        elif 'yml' in file_types or 'yaml' in file_types:
            scope = 'config'
        else:
            scope = 'core'
        
        # Generate description based on changes
        if analysis['files_changed'] == 1:
            file_name = Path(analysis['files'][0]).stem
            if analysis['change_type'] == 'add':
                description = f"add {file_name} implementation"
            elif analysis['change_type'] == 'remove':
                description = f"remove {file_name}"
            else:
                description = f"update {file_name}"
        else:
            if analysis['change_type'] == 'add':
                description = f"add {analysis['files_changed']} new files"
            elif analysis['change_type'] == 'feature':
                description = f"enhance functionality across {analysis['files_changed']} files"
            else:
                description = f"update {analysis['files_changed']} files"
        
        # Construct commit message
        commit_message = f"{commit_type}({scope}): {description}"
        
        # Add body with statistics
        body = f"\n\n- Files changed: {analysis['files_changed']}"
        body += f"\n- Lines added: {analysis['lines_added']}"
        body += f"\n- Lines removed: {analysis['lines_removed']}"
        
        return commit_message + body
    
    def commit_changes(self, message: str) -> bool:
        """Commit changes with generated message"""
        try:
            subprocess.run(['git', 'commit', '-m', message], check=True)
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Error committing changes: {e}")
            return False
    
    def run(self, auto_commit: bool = False, preview_only: bool = False):
        """Main execution method"""
        print(f"\n🤖 {self.app_name} v{self.version}")
        print(f"👨‍💻 Developed by: {self.developer}")
        print("=" * 50)
        
        # Check if in git repo
        if not self.check_git_repo():
            print("❌ Error: Not in a git repository")
            sys.exit(1)
        
        # Get staged changes
        print("📋 Analyzing staged changes...")
        diff_content = self.get_staged_changes()
        
        if not diff_content or not diff_content.strip():
            print("⚠️  No staged changes found. Use 'git add' to stage files first.")
            sys.exit(1)
        
        # Get staged files
        staged_files = self.get_staged_files()
        print(f"📁 Found {len(staged_files)} staged file(s)")
        
        # Analyze changes
        analysis = self.analyze_changes(diff_content, staged_files)
        
        # Generate commit message
        print("🧠 Generating intelligent commit message...")
        commit_message = self.generate_commit_message(analysis, diff_content)
        
        # Display results
        print("\n📝 Generated Commit Message:")
        print("-" * 30)
        print(commit_message)
        print("-" * 30)
        
        if preview_only:
            print("\n👀 Preview mode - no commit made")
            return
        
        # Commit or ask for confirmation
        if auto_commit:
            if self.commit_changes(commit_message):
                print("\n✅ Changes committed successfully!")
            else:
                print("\n❌ Failed to commit changes")
        else:
            response = input("\n❓ Commit with this message? (y/n/e for edit): ").lower()
            if response == 'y':
                if self.commit_changes(commit_message):
                    print("\n✅ Changes committed successfully!")
                else:
                    print("\n❌ Failed to commit changes")
            elif response == 'e':
                print("\n✏️  Edit mode - opening git commit editor...")
                subprocess.run(['git', 'commit'])
            else:
                print("\n🚫 Commit cancelled")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="GitCommit AI Assistant - Generate intelligent commit messages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Interactive mode
  python main.py --auto            # Auto-commit with generated message
  python main.py --preview         # Preview message only
  
Developed by: Deepak Nemade (DN)
        """
    )
    
    parser.add_argument('--auto', action='store_true', 
                       help='Automatically commit with generated message')
    parser.add_argument('--preview', action='store_true',
                       help='Preview generated message without committing')
    parser.add_argument('--version', action='version', version='GitCommit AI Assistant 1.0.0')
    
    args = parser.parse_args()
    
    try:
        app = GitCommitAI()
        app.run(auto_commit=args.auto, preview_only=args.preview)
    except KeyboardInterrupt:
        print("\n\n🛑 Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
