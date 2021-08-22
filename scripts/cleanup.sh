#!/usr/bin/env bash

echo "📝  Do you want cleanup your git commit history? [y/N]: "
read DEFAULT
if [[ $DEFAULT =~ ^([Yy])$ ]]; then
  echo "🚨 Cleanup your commit history"
  git checkout --orphan latest_branch
  git add -A
  git commit -am "chore: initial commit - include config files"
  git branch -D main
  git branch -m main
  git push -f origin main
fi
