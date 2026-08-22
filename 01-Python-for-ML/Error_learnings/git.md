# Git & GitHub Commands — Basic to Professional

A practical Git command reference covering the commands you will use most often, from creating a repository to branches, remotes, undoing changes, and professional workflows.

---

## 1. Check Git Installation

```bash
git --version
```

Check your Git configuration:

```bash
git config --list
```

Set your username:

```bash
git config --global user.name "Your Name"
```

Set your email:

```bash
git config --global user.email "your@email.com"
```

---

## 2. Start a Git Repository

Initialize Git in the current folder:

```bash
git init
```

Check repository status:

```bash
git status
```

Remove Git tracking from a folder (PowerShell):

```powershell
Remove-Item -Recurse -Force .git
```

> Be careful: removing `.git` deletes the local Git history for that repository.

---

## 3. Basic Git Workflow

The most important workflow:

```text
Edit files
   ↓
git status
   ↓
git add
   ↓
git commit
   ↓
git push
```

### Check changed files

```bash
git status
```

### Add one file

```bash
git add filename.py
```

### Add multiple files

```bash
git add file1.py file2.py
```

### Add everything

```bash
git add .
```

### Commit

```bash
git commit -m "Add data preprocessing"
```

### See what changed

```bash
git diff
```

See staged changes:

```bash
git diff --staged
```

---

## 4. Git History

Show commit history:

```bash
git log
```

### Compact history:
#### To get you git history in oneline you can use the following command

```bash
git log --oneline -5
```


Latest 5 commits:

```bash
git log --oneline -5
```

Recommended visual history:

```bash
git log --oneline --graph --all --decorate
```

Show details of a specific commit:

```bash
git show COMMIT_ID
```

---

## 5. Branches

List local branches:

```bash
git branch
```

List all branches:

```bash
git branch -a
```

Create a branch:

```bash
git branch feature-login
```

Switch to a branch:

```bash
git switch feature-login
```

Create and switch at the same time:

```bash
git switch -c feature-login
```

Delete a local branch:

```bash
git branch -d feature-login
```

Force-delete a branch:

```bash
git branch -D feature-login
```

Rename the current branch:

```bash
git branch -M main
```

---

## 6. Remote / GitHub

Check remote repositories:

```bash
git remote -v
```

Add a GitHub remote:

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Or using SSH:

```bash
git remote add origin git@github.com:USERNAME/REPOSITORY.git
```

Change an existing remote:

```bash
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

Remove a remote:

```bash
git remote remove origin
```

See remote details:

```bash
git remote show origin
```

---

## 7. Push to GitHub

First push of a new branch:

```bash
git push -u origin main
```

After upstream is configured:

```bash
git push
```

Push a specific branch:

```bash
git push origin feature-login
```

Push all local branches:

```bash
git push --all origin
```

Delete a remote branch:

```bash
git push origin --delete feature-login
```

---

## 8. Pull Changes from GitHub

Download and merge remote changes:

```bash
git pull
```

Pull a specific branch:

```bash
git pull origin main
```

Download remote information without changing your working files:

```bash
git fetch
```

Fetch everything:

```bash
git fetch --all
```

### Pull vs Fetch

```text
git fetch
    ↓
Downloads remote changes
    ↓
Does NOT modify your current branch

git pull
    ↓
Fetch + integrate changes
```

---

## 9. Clone a Repository

Clone using HTTPS:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Clone using SSH:

```bash
git clone git@github.com:USERNAME/REPOSITORY.git
```

Clone into a custom folder:

```bash
git clone REPOSITORY_URL folder-name
```

---

## 10. Undo Changes

### Discard changes in a file

```bash
git restore filename.py
```

Discard all unstaged changes:

```bash
git restore .
```

### Unstage a file

```bash
git restore --staged filename.py
```

### Undo the last commit but keep changes staged

```bash
git reset --soft HEAD~1
```

Undo the last commit and unstage the changes:

```bash
git reset HEAD~1
```

Undo the last commit and discard the changes:

```bash
git reset --hard HEAD~1
```

> `git reset --hard` can permanently remove uncommitted work. Use it carefully.

---

## 11. Fix the Last Commit

Change the last commit message:

```bash
git commit --amend -m "Better commit message"
```

Add forgotten changes to the previous commit:

```bash
git add .
git commit --amend --no-edit
```

If the previous commit was already pushed, amending it changes its commit history. Avoid rewriting shared history unless you know what you are doing.

---

## 12. Stash

Temporarily save uncommitted changes:

```bash
git stash
```

Save with a message:

```bash
git stash push -m "Work in progress"
```

List stashes:

```bash
git stash list
```

Restore the latest stash:

```bash
git stash pop
```

Apply a stash without deleting it:

```bash
git stash apply
```

Delete a stash:

```bash
git stash drop
```

---

## 13. Merge Branches

Switch to the branch that should receive the changes:

```bash
git switch main
```

Merge another branch:

```bash
git merge feature-login
```

If there are conflicts:

```text
1. Open the conflicted files
2. Resolve the conflicts
3. git add .
4. git commit
```

Abort an ongoing merge:

```bash
git merge --abort
```

---

## 14. Rebase — Professional Workflow

Update your feature branch on top of the latest main:

```bash
git switch feature-login
git fetch origin
git rebase origin/main
```

If conflicts occur:

```bash
git add .
git rebase --continue
```

Abort the rebase:

```bash
git rebase --abort
```

### Rebase vs Merge

```text
Merge:
main ────────●────────●
              \      /
feature        ●────●

Rebase:
main ────────●────────●
                       \
feature                 ●──●
```

Use rebase carefully on branches that other people are already using.

---

## 15. Tags

List tags:

```bash
git tag
```

Create a tag:

```bash
git tag v1.0.0
```

Create an annotated tag:

```bash
git tag -a v1.0.0 -m "Version 1.0.0"
```

Push a tag:

```bash
git push origin v1.0.0
```

Push all tags:

```bash
git push origin --tags
```

Delete a local tag:

```bash
git tag -d v1.0.0
```

---

## 16. .gitignore

Create a `.gitignore` file to prevent files from being tracked.

Common Python example:

```gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
.ipynb_checkpoints/
*.log
```

Common ML/data examples:

```gitignore
data/
datasets/
models/
*.pkl
*.pt
*.pth
```

Check ignored files:

```bash
git status --ignored
```

> Never commit secrets such as API keys, passwords, `.env` files, or private credentials.

---

## 17. Git Status & Tracking

Show status:

```bash
git status
```

Show tracked files:

```bash
git ls-files
```

Check whether a file is ignored:

```bash
git check-ignore -v filename
```

See who changed each line:

```bash
git blame filename.py
```

---

## 18. Find Commits

Search commit messages:

```bash
git log --oneline --grep="keyword"
```

Show commits from one author:

```bash
git log --author="Name" --oneline
```

Show commits affecting a file:

```bash
git log -- filename.py
```

---

## 19. Compare Branches

Compare two branches:

```bash
git diff main..feature-login
```

See commits that exist on one branch but not another:

```bash
git log main..feature-login --oneline
```

---

## 20. Remote Branch Cleanup

See remote branches:

```bash
git branch -r
```

Clean up deleted remote-tracking branches:

```bash
git fetch --prune
```

Then:

```bash
git branch -a
```

---

## 21. GitHub Workflow for a New Project

### Create local repository

```bash
cd project-folder
git init
git branch -M main
```

### Create `.gitignore`

Then:

```bash
git status
git add .
git commit -m "Initial commit"
```

### Connect GitHub

```bash
git remote add origin git@github.com:USERNAME/REPOSITORY.git
```

### Push

```bash
git push -u origin main
```

---

## 22. Daily Professional Workflow

For a personal project:

```bash
git status
git pull
```

Work on your files, then:

```bash
git status
git diff
git add .
git commit -m "Describe what changed"
git push
```

For a feature:

```bash
git switch main
git pull
git switch -c feature-name
```

Work and commit:

```bash
git add .
git commit -m "Add feature"
```

Update your branch:

```bash
git fetch origin
git rebase origin/main
```

Then push:

```bash
git push -u origin feature-name
```

---

## 23. Useful Commit Message Examples

Good:

```text
Add heart disease prediction model
Fix data preprocessing bug
Update model evaluation metrics
Add CNN image classifier
Refactor API authentication
Update README installation steps
Remove unused imports
```

Avoid vague messages:

```text
update
changes
done
final
new
test
```

A good commit message tells you **what changed**.

---

## 24. Common Problems

### "Not a git repository"

```text
fatal: not a git repository
```

Check your current folder:

```bash
pwd
```

PowerShell:

```powershell
Get-Location
```

Then:

```bash
git status
```

If this is supposed to be a new repository:

```bash
git init
```

---

### "Remote origin already exists"

Check it:

```bash
git remote -v
```

Change it:

```bash
git remote set-url origin NEW_URL
```

---

### Push rejected / non-fast-forward

First try:

```bash
git pull --rebase origin main
git push
```

If the remote and local repositories have completely unrelated histories, you may need:

```bash
git pull origin main --allow-unrelated-histories
```

Resolve any conflicts, commit if required, then:

```bash
git push
```

---

### LF will be replaced by CRLF

This is usually a line-ending warning on Windows.

Check:

```bash
git config --get core.autocrlf
```

A common Windows setting is:

```bash
git config --global core.autocrlf true
```

---

## 25. Git Aliases

Create a shorter command:

```bash
git config --global alias.st status
```

Now:

```bash
git st
```

instead of:

```bash
git status
```

Useful history alias:

```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
```

Then:

```bash
git lg
```

---

# ⭐ Most Important Commands to Memorize

If you are learning Git, master these first:

```bash
git init
git status
git add .
git commit -m "message"

git log --oneline
git branch
git switch -c branch-name
git switch branch-name

git remote -v
git remote add origin URL

git push
git pull
git fetch

git clone URL

git diff
git restore .
git restore --staged filename

git stash
git stash pop

git merge branch-name
git rebase origin/main

git reset --soft HEAD~1
git reset --hard HEAD~1
```

---

# Git Mental Model

Remember this:

```text
                    GitHub / Remote
                        ↑
                        push
                        │
                    ┌──────────┐
                    │  Remote  │
                    └──────────┘
                        │
                        pull
                        ↓
    ┌────────────┐    ┌──────────┐    ┌────────────┐
    │ Working     │ →  │ Staging  │ →  │ Repository │
    │ Directory  │    │  Area    │    │  (.git)    │
    └────────────┘    └──────────┘    └────────────┘
        │                │                │
    git diff         git add          git commit
```

The core cycle is:

```text
EDIT → STATUS → ADD → COMMIT → PUSH
```

That is the Git workflow you will use constantly.
