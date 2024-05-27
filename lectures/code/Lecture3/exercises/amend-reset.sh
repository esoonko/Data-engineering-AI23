#!/bin/bash

# Create a new directory for the scenario
mkdir git-amend-reset
cd git-amend-reset

# Initialize a new git repository
git init
git switch -c main

# Create an initial commit
echo "Initial content" > file.txt
git add file.txt
git commit -m "Initial commit"

# Make an incorrect commit
echo "Incorrect content" >> file.txt
git add file.txt
git commit -m "Incorrect commit"

# Output instructions for the student
cat <<EOL
You have made a commit with incorrect content. Your tasks are:
1. Amend the last commit to correct the commit message or the content.
2. Alternatively, you can reset the commit and create a new correct commit.

Commands you might need:
  git commit --amend
  git log
  git reset --soft <commit-hash>
  git add file.txt
  git commit -m "Correct commit"

Good luck!
EOL