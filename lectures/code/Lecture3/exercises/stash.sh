#!/bin/bash

# Create a new directory for the scenario
mkdir stash
cd stash

# Initialize a new git repository
git init
git switch -c main

# Create an initial commit
echo "Initial content" > file.txt
git add file.txt
git commit -m "Initial commit"

# Make changes to be stashed
echo "Unfinished work" >> file.txt

# Output instructions for the student
cat <<EOL
You have made some changes to 'file.txt' that you need to stash before switching branches.
Your tasks are:
1. Stash the changes in 'file.txt'.
2. Create and switch to a new branch.
3. Apply the stashed changes in the new branch.

Commands you might need:
  git stash
  git branch <branch-name>
  git checkout <branch-name>
  git stash apply

Good luck!
EOL