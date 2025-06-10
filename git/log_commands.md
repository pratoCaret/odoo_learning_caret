# Basic Usage:
git log
This displays the commit history starting from the most recent commit.


# Common Options:
Show commits in one line (short summary)

git log --oneline

Displays a compact history with commit hashes and messages.


# Limit the number of commits displayed
git log -n 5

Shows only the last 5 commits.


# Filter commits by author
git log --author="John Doe"

Displays commits made by a specific author.


# Search commits by message
git log --grep="bug fix"

Shows commits that contain "bug fix" in their message.


# Show changes introduced by each commit
git log -p

Displays the actual code changes (diffs) along with commit history.


# Show history in a graphical representation
git log --graph --oneline --all --decorate

Displays a visual branch structure of the commit history.


