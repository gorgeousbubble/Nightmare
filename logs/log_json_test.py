#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest
from logs.log_json import LogJson


class TestLogJson(unittest.TestCase):
    def test_init(self):
        log = LogJson(file='./json/log.json', path='../log').get_logger(__name__)
        log.debug('hello,world~')
        log.info('python json.')
