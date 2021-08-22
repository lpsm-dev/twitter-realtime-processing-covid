#!/usr/bin/env bash

echo "📝  Do you want gen a new release? [y/N]: "
read DEFAULT
if [[ $DEFAULT =~ ^([Yy])$ ]]; then
  echo "🚨 Making the release - Please, export your GITLAB_TOKEN before run this script"
  make release-debug
  git add . && git commit -am "chore: bump version file"
  make release
  git push --all
  git pull --all
fi