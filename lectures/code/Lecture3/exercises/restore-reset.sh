#!/bin/bash

# Create a new directory for the scenario
mkdir restore-reset
cd restore-reset

# Initialize a new git repository
git init
git switch -c main

# Create an initial commit
echo "Initial content" > file.txt
git add file.txt
git commit -m "Initial commit"

# Make a commit to be reset later
echo "Content to be reset" >> file.txt
git add file.txt
git commit -m "Commit to be reset"

# Make changes to be restored
echo "Unstaged changes" >> file.txt

# Output instructions for the student
cat <<EOL
You have made some changes to 'file.txt' that are not staged yet. Additionally, there is a commit that needs to be reset.
Your tasks are:
1. Restore the unstaged changes to 'file.txt'.
2. Reset the last commit, bringing the repository back to the state it was before that commit.

Commands you might need:
  git restore file.txt
  git log
  git reset --hard <commit-hash>

Good luck!
EOL