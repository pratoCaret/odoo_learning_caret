# Fixing a commit message
If you made a typo in the last commit message, you can update it:

git commit --amend -m "Updated commit message"


# Adding new changes to the last commit
If you forgot to add some changes to your last commit:

git add <file>

git commit --amend


# Removing a file from the last commit
If you accidentally included a file, remove it and amend the commit:

git reset HEAD~ -- <file>
git commit --amend


# Important Notes:
git commit --amend rewrites history, so avoid using it after pushing to a shared repository unless you're sure.

If you've already pushed the commit, you need to force push (git push --force) after amending, which can cause issues in collaborative workflows.




# git commit --amend -m "your message" Changes:

this is the first change to commit after the main commit. not to be reverted or amended.
