#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest
from logs.log_yaml import LogYaml


class TestLogYaml(unittest.TestCase):
    def test_init(self):
        log = LogYaml(file='./yaml/log.yaml', path='../log').get_logger(__name__)
        log.debug('hello,world~')
        log.info('python yaml.')
