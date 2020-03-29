# Nightmare Project - Makefile(Python)
# Copyright(C) 2020, Team Gorgeous Bubble, All Rights Reserved.

# Python Commands
PYTHON = python3

# Binary Parameters
PYBASE  = $(shell pwd)
PYBIN   = $(PYBASE)/bin
MKBIN   = $(shell mkdir -p $(PYBIN))

# Docker Commands
DOCKER      = docker
DOCKERBUILD = $(DOCKER) build
DOCKERRUN   = $(DOCKER) run

# Application
APPNAME = nightmare
APPDIST = $(APPNAME).tar.gz
APPPATH = $(PYBIN)/$(APPNAME)

# Build
all: build

.PHONY: build
build:
	pyinstaller -n $(APPNAME) -F main.py

.PHONY: clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf log
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr

.PHONY: test
test:
	$(PYTHON) -m pytest

.PHONY: lint
lint:
	$(PYTHON) -m pylint
