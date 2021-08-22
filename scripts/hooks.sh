#!/usr/bin/env bash

echo "📝  Do you want add git hooks? [y/N]: "
read DEFAULT
if [[ $DEFAULT =~ ^([Yy])$ ]]; then
  echo "🚨 Adding husky git hooks"
  pre-commit install
  pre-commit install --hook-type commit-msg
fi
