#!/bin/bash

# Create a new directory for the scenario
mkdir merge-conflict
cd merge-conflict

# Initialize a new git repository
git init
git checkout -b main

# Create an initial commit
echo "This is the initial content of the file." > conflict-file.txt
git add conflict-file.txt
git commit -m "Initial commit"

# Create a new branch and make a conflicting change
git checkout -b branch-1
echo "Change from branch-1" > conflict-file.txt
git commit -am "Change from branch-1"

# Switch back to the main branch and make a conflicting change
git checkout main
echo "Change from main branch" > conflict-file.txt
git commit -am "Change from main branch"

# Merge branch-1 into main to create a conflict
git merge branch-1 || true

# Output instructions for the student
cat <<EOL
A merge conflict has been created between the main branch and branch-1.
Your task is to resolve the conflict in 'conflict-file.txt' and complete the merge.

Commands you might need:
  git status
  git diff
  nano conflict-file.txt (or your preferred editor)
  git add conflict-file.txt
  git commit

Good luck!
EOL
