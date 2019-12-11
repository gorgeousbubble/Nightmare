#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from logs.log import Log


class TestLog(unittest.TestCase):
    def test_init_console(self):
        log = Log(target='console').get_logger(__name__)
        log.debug('hello,world')