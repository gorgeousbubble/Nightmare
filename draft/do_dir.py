#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def test_os_name():
    print(os.name)


def test_os_environ():
    print(os.environ.get('PATH'))


def test_os_split():
    print(os.path.split('../test/data/draft/hello.txt'))


def test_os_splitext():
    print(os.path.splitext('../test/data/draft/hello.txt'))


if __name__ == '__main__':
    test_os_name()
    test_os_environ()
    test_os_split()
    test_os_splitext()
