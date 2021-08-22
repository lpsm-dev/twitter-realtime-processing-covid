MAKEFLAGS += --warn-undefined-variables

# It's necessary to set this because some environments don't link sh -> bash.
SHELL := /usr/bin/env bash

##################################################
# HELPER
##################################################

.PHONY: help
help:
	@echo ""
	@echo "****************************************"
	@echo "* 🤖 Management commands"
	@echo "* "
	@echo "* Usage:"
	@echo "* "
	@echo "*  🎉 Short commands 🎉"
	@echo "* "
	@echo "* 📌 make verify"
	@echo "* 📌 make global-requirements"
	@echo "* 📌 make npm-requirements"
	@echo "* 📌 make version"
	@echo "* 📌 make install"
	@echo "* 📌 make scan"
	@echo "* 📌 make release-debug"
	@echo "* 📌 make release"
	@echo "* "
	@echo "****************************************"
	@echo ""

##################################################
# SHORTCUTS
##################################################

verify:
ifeq ($(GITHUB_TOKEN),)
	@echo "ERROR: 🆘 no GITHUB_TOKEN was provided - undefined variable. Exiting." && exit 1
else
	@echo "==> 🎊 We have a GITHUB_TOKEN!"
endif

global-requirements:
	@echo "==> 🌐 Checking global requirements..."
	@command -v git >/dev/null || ( echo "ERROR: 🆘 git binary not found. Exiting." && exit 1)
	@command -v gitleaks >/dev/null || ( echo "ERROR: 🆘 gitleaks binary not found. Exiting." && exit 1)
	@echo "==> ✅ Global requirements are met!"

npm-requirements: global-requirements
	@echo "==> 📜 Checking npm requirements..."
	@command -v npm >/dev/null || ( echo "ERROR: 🆘 npm binary not found. Exiting." && exit 1)
	@echo "==> ✅ Package requirements are met!"

version: npm-requirements
	@echo "==> ✨ Git version: $(shell git --version)"
	@echo "==> ✨ Gitleaks version: $(shell gitleaks --version)"
	@echo "==> ✨ NPM version: $(shell npm --version)"

install: npm-requirements
	@echo "==> 🔥 NPM install packages..."
	@npm install

scan: global-requirements
	@echo "==> 🔒 Scan git repo for secrets..."
	@npm run secrets

release-debug: install verify
	@echo "==> 📦 Runnig release debug..."
	@npm run release-debug

release: install verify
	@echo "==> 📦 Runnig release..."
	@npm run release
