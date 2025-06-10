# git command from the start:
1. add
2. commit
3. push

# to confirm installed git:
git --version

# git configure:
git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"

# convert a folder into git repo:
git init
# add a Remote Repository:
git remote add origin git@gitlab.com:username/projectpath.git

# clone a repo:
git clone <ssh or html link>

# navigate to repository:
cd sample-project

# pull all changes:
git pull <REMOTE> <name-of-branch>

# Work with Branches:
Create a New Branch:
git checkout -b <branch-name>
    
Switch to an Existing Branch:
git checkout <branch-name>

Merge a Branch with the Default Branch:
git checkout <default-branch>
git merge <feature-branch>

# View Changes:
Check Differences:
git diff

Check Changed Files:
git status

# Stage and Commit Changes

Stage/add a File:
git add <file-name>

Stage/All add Files:
git add .

how many files in commit area:
git show --name-only

Commit the Staged Files:
git commit -m "Your commit message"

Stage & Commit in One Step:
git commit -a -m "Your commit message"

# Push Changes to Remote:
git push <remote> <branch-name>
git push origin main

// Uploads your commits to the remote repository.

# Undo Changes
Discard All Local Changes (Tracked Files):
git checkout .

# Unstage All Files:
git reset

# Undo the Most Recent Commit:
git reset HEAD~1

// This does not delete changes, just unstages them.
