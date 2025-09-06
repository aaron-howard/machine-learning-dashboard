#!/usr/bin/env python3
"""
GitHub Repository Preparation Script
This script helps prepare the ML Dashboard project for GitHub
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_git_status():
    """Check if this is a git repository"""
    if not os.path.exists('.git'):
        print("📁 Initializing git repository...")
        if not run_command('git init', 'Git initialization'):
            return False
    
    return True

def create_initial_commit():
    """Create initial commit with all files"""
    print("📝 Creating initial commit...")
    
    # Add all files
    if not run_command('git add .', 'Adding files to git'):
        return False
    
    # Create initial commit
    if not run_command('git commit -m "Initial commit: ML Dashboard v1.0.0"', 'Creating initial commit'):
        return False
    
    return True

def create_gitignore_if_missing():
    """Ensure .gitignore exists"""
    if not os.path.exists('.gitignore'):
        print("⚠️  .gitignore not found, creating one...")
        # The .gitignore should already exist from our previous work
        return False
    return True

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        'README.md',
        'LICENSE',
        'CONTRIBUTING.md',
        'CHANGELOG.md',
        'SECURITY.md',
        'setup.py',
        'requirements.txt',
        'app.py',
        '.gitignore',
        '.github/workflows/ci.yml',
        '.github/workflows/code-quality.yml',
        '.github/workflows/dependency-review.yml',
        '.github/ISSUE_TEMPLATE/bug_report.md',
        '.github/ISSUE_TEMPLATE/feature_request.md',
        '.github/pull_request_template.md',
        '.github/FUNDING.yml'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files present")
    return True

def create_repository_instructions():
    """Create instructions for setting up GitHub repository"""
    instructions = """
# 🚀 GitHub Repository Setup Instructions

## 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `machine-learning-dashboard`
   - **Description**: `A comprehensive web-based dashboard for visualizing machine learning model performance and predictions with interactive charts and real-time data updates`
   - **Visibility**: Public (or Private if preferred)
   - **Initialize**: Don't initialize with README, .gitignore, or license (we already have these)

## 2. Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/machine-learning-dashboard.git

# Set the main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

## 3. Configure Repository Settings

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Configure the following:

### General Settings
- **Repository name**: `machine-learning-dashboard`
- **Description**: Update if needed
- **Website**: `http://localhost:5000` (for local development)
- **Topics**: Add tags like `machine-learning`, `dashboard`, `tensorflow`, `flask`, `d3.js`, `bootstrap`

### Features
- ✅ Issues
- ✅ Projects
- ✅ Wiki
- ✅ Discussions (optional)

### Branches
- Set `main` as the default branch
- Add branch protection rules for `main` branch

## 4. Update Badge URLs

After pushing to GitHub, update the badge URLs in `README.md`:

1. Replace `your-username` with your actual GitHub username
2. Update the CI/CD badge URL
3. Update all other badge URLs

## 5. Create First Release

1. Go to "Releases" in your repository
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `ML Dashboard v1.0.0`
5. Description: Copy from `CHANGELOG.md`
6. Publish release

## 6. Enable GitHub Actions

1. Go to "Actions" tab
2. Enable GitHub Actions if prompted
3. The workflows will run automatically on push/PR

## 7. Configure Security Settings

1. Go to "Security" tab
2. Enable Dependabot alerts
3. Enable secret scanning
4. Enable code scanning (if desired)

## 8. Optional: GitHub Pages

If you want to host documentation:

1. Go to "Settings" > "Pages"
2. Source: Deploy from a branch
3. Branch: `main` / `docs` folder
4. Save

## 9. Community Guidelines

1. Go to "Community" in repository settings
2. Enable issue templates
3. Enable pull request templates
4. Set up code of conduct (already included)

## 10. Final Checklist

- [ ] Repository created and connected
- [ ] All files pushed to GitHub
- [ ] Badge URLs updated in README
- [ ] First release created
- [ ] GitHub Actions enabled
- [ ] Security settings configured
- [ ] Community guidelines enabled
- [ ] Repository is public and accessible

## Next Steps

1. **Test the setup**: Clone the repository in a new location and test
2. **Create issues**: Add some initial issues for future development
3. **Invite collaborators**: Add team members if working in a group
4. **Monitor**: Watch the repository for issues and contributions

## Troubleshooting

If you encounter issues:

1. **Authentication**: Make sure you're logged into GitHub
2. **Permissions**: Ensure you have write access to the repository
3. **Git**: Make sure Git is configured with your name and email
4. **Network**: Check your internet connection

## Support

For help with GitHub setup:
- [GitHub Documentation](https://docs.github.com/)
- [GitHub Community Forum](https://github.community/)
- [GitHub Support](https://support.github.com/)

---

**Happy coding!** 🎉
"""
    
    with open('GITHUB_SETUP_INSTRUCTIONS.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("📋 Created GITHUB_SETUP_INSTRUCTIONS.md")

def main():
    """Main function"""
    print("🚀 ML Dashboard - GitHub Preparation Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check git status
    if not check_git_status():
        print("❌ Failed to initialize git repository")
        sys.exit(1)
    
    # Check required files
    if not check_required_files():
        print("❌ Some required files are missing. Please ensure all files are created first.")
        sys.exit(1)
    
    # Create initial commit
    if not create_initial_commit():
        print("❌ Failed to create initial commit")
        sys.exit(1)
    
    # Create setup instructions
    create_repository_instructions()
    
    print("\n" + "=" * 50)
    print("✅ GitHub preparation completed successfully!")
    print("\n📋 Next steps:")
    print("1. Read GITHUB_SETUP_INSTRUCTIONS.md")
    print("2. Create a GitHub repository")
    print("3. Connect your local repository to GitHub")
    print("4. Push your code to GitHub")
    print("5. Configure repository settings")
    print("\n🎉 Your ML Dashboard is ready for GitHub!")

if __name__ == '__main__':
    main()
