# GitCommit AI Assistant 🤖

**A privacy-focused local application that intelligently generates Git commit messages**

*Developed by: Deepak Nemade (DN)*

## 🌟 Features

- **🔒 Privacy First**: Uses local AI logic (rule-based) - no data sent to external services
- **🧠 Intelligent Analysis**: Analyzes staged changes, file types, and modification patterns
- **📝 Smart Messages**: Generates conventional commit messages with proper formatting
- **⚡ Fast & Lightweight**: No external dependencies or API calls required
- **🎯 Production Ready**: Comprehensive error handling and logging
- **🔧 Flexible Usage**: Interactive, auto-commit, and preview modes

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Git repository

### Installation

1. Clone or download the application:
```bash
cd GitCommit-AI-Assistant
```

2. Make the script executable:
```bash
chmod +x main.py
```

### Usage

#### Interactive Mode (Recommended)
```bash
python main.py
```
Analyzes changes and asks for confirmation before committing.

#### Auto-Commit Mode
```bash
python main.py --auto
```
Automatically commits with the generated message.

#### Preview Mode
```bash
python main.py --preview
```
Shows the generated message without committing.

## 📋 How It Works

1. **🔍 Detection**: Checks if you're in a Git repository
2. **📊 Analysis**: Reads staged changes using `git diff --cached`
3. **🧮 Processing**: Analyzes file types, change patterns, and statistics
4. **🎯 Generation**: Creates intelligent commit messages using local AI logic
5. **✅ Execution**: Commits changes or provides preview

## 🎨 Generated Message Format

The application generates conventional commit messages:

```
type(scope): description

- Files changed: X
- Lines added: Y  
- Lines removed: Z
```

### Commit Types
- `feat`: New features or additions
- `chore`: Updates and modifications
- `refactor`: Code refactoring or removals

### Smart Scopes
- `python`: Python files (.py)
- `frontend`: JavaScript/TypeScript files (.js, .ts)
- `docs`: Documentation files (.md)
- `config`: Configuration files (.yml, .yaml)
- `core`: Other file types

## 📖 Examples

### Single File Addition
```bash
$ git add new_feature.py
$ python main.py
```
Output: `feat(python): add new_feature implementation`

### Multiple File Update
```bash
$ git add *.js
$ python main.py  
```
Output: `chore(frontend): update 3 files`

### Documentation Changes
```bash
$ git add README.md
$ python main.py
```
Output: `chore(docs): update README`

## 🛠️ Command Line Options

| Option | Description |
|--------|-------------|
| `--auto` | Auto-commit with generated message |
| `--preview` | Preview message without committing |
| `--version` | Show version information |
| `--help` | Show help message |

## 🔧 Advanced Usage

### Integration with Git Aliases
Add to your `.gitconfig`:
```ini
[alias]
    ai-commit = !python /path/to/GitCommit-AI-Assistant/main.py
    ai-preview = !python /path/to/GitCommit-AI-Assistant/main.py --preview
```

Usage:
```bash
git ai-commit
git ai-preview
```

### Shell Integration
Add to your `.bashrc` or `.zshrc`:
```bash
alias gai='python /path/to/GitCommit-AI-Assistant/main.py'
alias gaip='python /path/to/GitCommit-AI-Assistant/main.py --preview'
```

## 🔒 Privacy & Security

- **100% Local**: No external API calls or data transmission
- **No Storage**: Doesn't store or cache any of your code
- **Open Source**: Full transparency in how messages are generated
- **Secure**: Uses only standard Git commands

## 🐛 Troubleshooting

### Common Issues

**"Not in a git repository"**
- Ensure you're in a Git repository directory
- Run `git init` if needed

**"No staged changes found"**
- Stage files first: `git add <files>`
- Check staged files: `git status`

**Permission denied**
- Make script executable: `chmod +x main.py`
- Check Python installation: `python --version`

## 🤝 Contributing

This is a production-ready application developed by Deepak Nemade (DN). 

### Development Setup
```bash
git clone <repository>
cd GitCommit-AI-Assistant
python main.py --help
```

## 📄 License

MIT License - Feel free to use and modify for your projects.

## 👨‍💻 Developer

**Deepak Nemade (DN)**
- Focused on privacy-first development
- Committed to creating efficient, local-first tools
- Passionate about developer productivity

---

## 🎯 Why GitCommit AI Assistant?

- **Privacy**: Your code never leaves your machine
- **Speed**: Instant analysis and generation
- **Intelligence**: Context-aware message creation
- **Simplicity**: One command, perfect commits
- **Reliability**: Production-tested and robust

**Start writing better commit messages today! 🚀**
