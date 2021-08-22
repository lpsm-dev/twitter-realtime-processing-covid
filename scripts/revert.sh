#!/usr/bin/env bash

echo "📝  Do you want revert master branch to a stable tag? [y/N]: "
read DEFAULT
if [[ $DEFAULT =~ ^([Yy])$ ]]; then
  echo "🚨 Revert master branch to a stable tag"
  STABLE_TAG="v1.7.0"
  git log --oneline
  git checkout master
  git reset --hard $STABLE_TAG
  git push --force origin master
  git log --oneline
fi
