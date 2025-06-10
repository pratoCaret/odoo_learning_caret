this is to check ki konsi file upload hori hai

git command used is as follows:
1. git init - create the local repo 
2. git branch -m 'branch-3'
3. git checkout -b <branch name>
4. git remote add origin <git ssh> - in the folder I want to upload through terminal.
5. git branch --set-upstream-to=origin/deskto-git-branch
6. git add .
7. git commit -m "comment"
8. git push origin desktop-git-branch


future workflow:
git add .
git commit -m "Updated files"
git push origin desktop-git-branch
