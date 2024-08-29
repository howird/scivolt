---
status: backlog
tags:
  - '#type/tutorial'
  - '#area/swe/tool'
---

# Git

> \[!info\]
> Put any git commands here that you need to remember and could foresee yourself using in the future.

### Normal usage

```bash
git checkout -b <local name> origin/<actual name>
git push -u origin <local name>
git add then git commit -m “message” OR
git commit -am “message”
git push origin HEAD:<actual name>
```

### Reverting push

- Get previous commit hashes:

```bash
git log
```

- then remove the sha(s) of the commit(s) you don’t want

```bash
git rebase -i <sha of commit before the commit(s) you don't want>
```

- then force push the changes to YOUR BRANCH, DO NOT DO THIS TO MAIN

```bash
git push -f origin HEAD:<actual name>
```

### Rewrite commit message

```bash
git commit --amend
```

### Moving changes from local master to other branch

```bash
git stash
git checkout <branch123>
git stash apply
```

### To discard local changes to all files, permanently

```bash
git reset --hard
```

### Delete local branch

```bash
git branch -d <local-branch>
```

### Delete remote branch

```bash
git push -d origin <branch_name>
```

### Remove files that are listed in the .gitignore but still on the repository

- to do these kind of tasks you should actually just use [`git-filter-repo`](https://github.com/newren/git-filter-repo/blob/main/git-filter-repo), a single python script

```bash
git rm -r --cached .
git add .
git commit -m "Drop files from .gitignore"
```

### Start new git repo from local folder

- Go on github and create new git repo

```bash
git init
git add --all
git commit -am "initial commit"
git remote add origin git@<remote repo>.git
git push –set-upstream origin main
```

### Get the git repo's remote url

```bash
git config remote.origin.url
```

### Set the git repo's remote url

```bash
git remote set-url origin git@<remote repo>.git
```

Cherry pick
