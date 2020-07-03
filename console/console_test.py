#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from console import Console
from console import ConsoleLevel


class TestConsole(unittest.TestCase):
    def test_simple_print(self):
        Console.debug('hello,world')

    def test_level_print(self):
        Console.level = ConsoleLevel.INFO
        Console.debug('hello,world')
        Console.info('python')

    def test_disable_print(self):
        Console.enable = False
        Console.debug('hello,world')
        Console.info('python')
