# Git Configration
git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"

# Clone a repository:
git clone <ssh or html link>

# Convert a local directory into a repository:
git init

# Add a remote:
git remote add origin branch-name

# Status:
git status

# Commit:
git commit -m "comment"

# how many files in commit area:
git show --name-only

# Push:
git push origin branch-name

# Download the latest changes in the project (Pull):
git pull origin branch-name
git pull --rebase origin branch-name // rebase

# Branch:
git branch // list branches | -r for remote and -a for all

# Create a branch:
git branch -m branch-name

# Create and Switch to a New Branch (Shortcut) :
git checkout -b branch-name

OR (Preferred in newer Git versions)

git switch -c branch-name

# Rename Branch:
git branch -m old-name new-name

# Switch to a branch:
git checkout branch-name

OR

git switch branch-name


# Delete Branch:
local : git branch -d branch-name

remote : git push origin --delete branch-name

# Unstage all changes (git reset):
git reset OR git reset file-name

# Undo most recent commit:
git reset HEAD~1

# Merge a branch:
git merge branch-name

# 
