# Nightmare Project - Makefile(Python)
# Copyright(C) 2020, Team Gorgeous Bubble, All Rights Reserved.

# Python Commands
PYTHON = python

# Docker Commands
DOCKER      = docker
DOCKERBUILD = $(DOCKER) build
DOCKERRUN   = $(DOCKER) run

# Application
APPNAME = nightmare
APPDIST = $(APPNAME).tar.gz
APPPATH = ./bin/$(APPNAME)