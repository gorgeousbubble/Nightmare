# Nightmare Project - Makefile(Python)
# Copyright(C) 2020, Team Gorgeous Bubble, All Rights Reserved.

# Python Commands
PYTHON = python

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

.PHONY: clean-build
clean-build:
	rm -rf build
	rm -rf dist

.PHONY: clean-log
clean-log:
	rm -rf log

.PHONY: clean-pyc
clean-pyc:
	@find . -name '*.pyc' -delete
    @find . -name '__pycache__' -type d | xargs rm -fr
    @find . -name '.pytest_cache' -type d | xargs rm -fr

.PHONY: clean
clean:
	clean-build
	clean-log
	clean-pyc
