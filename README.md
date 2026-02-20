# GitCommit AI Assistant

**Professional local application for intelligent Git commit message generation**

*Developed by: Deepak Nemade (DN)*

## Features

- **Privacy First**: Local processing - no external API calls
- **Auto-Detection**: Automatically generates messages for all `git commit` commands
- **Intelligent Analysis**: Analyzes staged changes and file patterns
- **Professional Messages**: Generates conventional commit format
- **Git Integration**: Supports GPG signing and signoff options

## Quick Start

### Prerequisites
- Python 3.6+
- Git repository

### Installation
```bash
git clone https://github.com/DeepDN/GitCommit-AI-Assistant.git
cd GitCommit-AI-Assistant
python3 install.py
```

**That's it!** After installation, the AI assistant automatically generates commit messages for all `git commit` commands. No need to run the application manually.

## How It Works

After installation, the AI assistant integrates with Git hooks to automatically:

1. **Detect Commits**: Triggers on every `git commit` command
2. **Analyze Changes**: Reads staged changes via `git diff --cached`
3. **Generate Messages**: Creates conventional commit format messages
4. **Apply Commit**: Executes with your original Git options (signing, signoff, etc.)

## Message Format

Generated messages follow conventional commit standards:

```
type(scope): description
```

### Commit Types
- `feat`: New features or file additions
- `chore`: Updates and general maintenance
- `refactor`: Code restructuring or removals

### Intelligent Scopes
- `python`: Python files (.py)
- `frontend`: JavaScript/TypeScript (.js, .ts)
- `docs`: Documentation (.md)
- `config`: Configuration files (.yml, .yaml)
- `core`: Other file types

## Usage Examples

After installation, just use normal Git commands:

```bash
git add feature.py
git commit                    # Auto-generates: feat(python): add feature implementation

git add *.js  
git commit -S                 # Auto-generates with GPG signing

git add README.md
git commit -s                 # Auto-generates with signed-off-by
```

## Security & Privacy

- **100% Local Processing**: No external network calls
- **No Data Storage**: Doesn't cache or store code
- **Open Source**: Full transparency in implementation
- **Secure Git Integration**: Uses standard Git commands only

## Troubleshooting

### Common Issues

**"Not in a git repository"**
- Navigate to Git repository directory
- Initialize with `git init` if needed

**"No staged changes found"**
- Stage files: `git add <files>`
- Verify with `git status`

**GPG signing fails**
- Configure GPG key: `git config user.signingkey <key-id>`
- Set up GPG agent for key management

## License

MIT License - Open source and free to use.

## Developer

**Deepak Nemade (DN)**
- Professional software developer
- Focus on developer productivity tools
- Committed to privacy-first solutions

---

**Professional Git workflow enhancement for modern development teams.**
