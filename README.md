# GitCommit AI Assistant

**Professional local application for intelligent Git commit message generation**

*Developed by: Deepak Nemade (DN)*

## Features

- **Privacy First**: Local processing - no external API calls
- **Intelligent Analysis**: Analyzes staged changes and file patterns
- **Professional Messages**: Generates conventional commit format
- **Git Integration**: Supports GPG signing and signoff options
- **Production Ready**: Comprehensive error handling and logging
- **Multiple Modes**: Interactive, auto-commit, and preview modes

## Quick Start

### Prerequisites
- Python 3.6+
- Git repository

### Installation

```bash
git clone https://github.com/DeepDN/GitCommit-AI-Assistant.git
cd GitCommit-AI-Assistant
chmod +x main.py setup.sh
./setup.sh
```

### Usage

#### Basic Usage
```bash
python main.py                    # Interactive mode
python main.py --auto            # Auto-commit mode
python main.py --preview         # Preview mode only
```

#### Advanced Git Options
```bash
python main.py --sign            # GPG sign commit
python main.py -s                # Add signed-off-by line
python main.py --auto --sign -s  # Auto-commit with signature and signoff
```

## How It Works

1. **Repository Detection**: Validates Git repository
2. **Change Analysis**: Reads staged changes via `git diff --cached`
3. **Pattern Recognition**: Analyzes file types and modification patterns
4. **Message Generation**: Creates conventional commit messages
5. **Commit Execution**: Applies changes with optional signing

## Message Format

Generated messages follow conventional commit standards:

```
type(scope): description

- Files changed: X
- Lines added: Y  
- Lines removed: Z
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

## Examples

### Single File Addition
```bash
git add feature.py
python main.py
```
Output: `feat(python): add feature implementation`

### Multiple File Update with Signing
```bash
git add *.js
python main.py --auto --sign
```
Output: `chore(frontend): update 3 files` (GPG signed)

### Documentation with Signoff
```bash
git add README.md
python main.py -s
```
Output: `chore(docs): update README` (with signed-off-by)

## Command Line Options

| Option | Description |
|--------|-------------|
| `--auto` | Auto-commit with generated message |
| `--preview` | Preview message without committing |
| `--sign` | GPG sign the commit (-S) |
| `-s, --signoff` | Add signed-off-by line |
| `--version` | Show version information |
| `--help` | Show help message |

## Advanced Integration

### Git Aliases
Add to `.gitconfig`:
```ini
[alias]
    ai = !python /path/to/GitCommit-AI-Assistant/main.py
    ais = !python /path/to/GitCommit-AI-Assistant/main.py --sign
    aip = !python /path/to/GitCommit-AI-Assistant/main.py --preview
```

### Shell Aliases
Add to `.bashrc` or `.zshrc`:
```bash
alias gai='python /path/to/GitCommit-AI-Assistant/main.py'
alias gais='python /path/to/GitCommit-AI-Assistant/main.py --sign'
alias gaip='python /path/to/GitCommit-AI-Assistant/main.py --preview'
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

## Development

### Project Structure
```
GitCommit-AI-Assistant/
├── main.py           # Core application
├── README.md         # Documentation
├── requirements.txt  # Dependencies
├── setup.sh         # Setup script
└── .git/            # Git repository
```

### Contributing
1. Fork the repository
2. Create feature branch
3. Make changes with proper commit messages
4. Submit pull request

## License

MIT License - Open source and free to use.

## Developer

**Deepak Nemade (DN)**
- Professional software developer
- Focus on developer productivity tools
- Committed to privacy-first solutions

---

**Professional Git workflow enhancement for modern development teams.**
