#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from logs.log import Log


class TestLog(unittest.TestCase):
    def test_init_console(self):
        log = Log(target='console').get_logger(__name__)
        log.debug('hello,world')

    def test_init_file(self):
        log = Log(target='file').get_logger(__name__)
        log.debug('hello,world')

    def test_init_rotating_file(self):
        log = Log(target='rotating_file').get_logger(__name__)
        log.debug('hello,world')
