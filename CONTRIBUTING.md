# Contributing to ML Dashboard

Thank you for your interest in contributing to the ML Dashboard! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Development Standards](#development-standards)

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/machine-learning-dashboard.git
   cd machine-learning-dashboard
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test the installation**
   ```bash
   python test_installation.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## Contributing Guidelines

### Types of Contributions

We welcome several types of contributions:

- **Bug Reports**: Report bugs and issues
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit bug fixes or new features
- **Documentation**: Improve documentation and examples
- **Testing**: Add or improve tests

### Before You Start

1. Check existing issues and pull requests to avoid duplicates
2. For major changes, open an issue first to discuss the approach
3. Ensure your changes align with the project's goals

### Development Standards

#### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

#### JavaScript/HTML/CSS

- Use consistent indentation (2 spaces)
- Follow modern ES6+ practices
- Use meaningful class and ID names
- Comment complex CSS rules

#### Testing

- Test your changes thoroughly
- Add tests for new features when possible
- Ensure existing tests still pass
- Test on different browsers (for frontend changes)

#### Documentation

- Update README.md if you add new features
- Add docstrings to new functions
- Update API documentation if you modify endpoints
- Include examples for new features

## Pull Request Process

### Before Submitting

1. **Test your changes**
   ```bash
   python test_installation.py
   python app.py  # Test the application
   ```

2. **Check code style**
   - Ensure your code follows the project's style guidelines
   - Remove any debugging code or print statements

3. **Update documentation**
   - Update README.md if needed
   - Add or update docstrings
   - Update any relevant documentation

### Pull Request Template

When creating a pull request, please include:

- **Description**: What changes were made and why
- **Type**: Bug fix, feature, documentation, etc.
- **Testing**: How the changes were tested
- **Screenshots**: For UI changes
- **Breaking Changes**: Any breaking changes and migration steps

### Review Process

1. All pull requests require review
2. Address feedback promptly
3. Keep pull requests focused and small
4. Respond to review comments constructively

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: OS, Python version, browser (if applicable)
- **Screenshots**: If applicable

### Feature Requests

When requesting features, please include:

- **Description**: Clear description of the feature
- **Use Case**: Why this feature would be useful
- **Proposed Solution**: How you think it should work
- **Alternatives**: Other solutions you've considered

## Development Standards

### Git Workflow

1. **Branch Naming**: Use descriptive branch names
   - `feature/add-new-chart-type`
   - `bugfix/fix-performance-issue`
   - `docs/update-readme`

2. **Commit Messages**: Use clear, descriptive commit messages
   - `feat: add confusion matrix visualization`
   - `fix: resolve real-time update issue`
   - `docs: update installation instructions`

3. **Pull Request Title**: Use the same format as commit messages

### Code Organization

- Keep related functionality together
- Use appropriate file and folder structure
- Follow the existing code patterns
- Add appropriate error handling

### Performance Considerations

- Consider performance impact of changes
- Optimize for both development and production
- Test with different data sizes
- Monitor memory usage

## Getting Help

If you need help:

1. Check the [README.md](README.md) for basic information
2. Look at existing issues and discussions
3. Create a new issue with your question
4. Join our community discussions (if available)

## Recognition

Contributors will be recognized in:

- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to the ML Dashboard project!

---

**Contact**: For questions about contributing, please open an issue or contact the maintainers.
