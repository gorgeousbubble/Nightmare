#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
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

    def test_multiple_output(self):
        ins = Log(target='console')
        ins.add_handler_file()
        log = ins.get_logger(__name__)
        log.debug('hello,world')

    def test_level(self):
        log = Log(target='console', level=logging.ERROR).get_logger(__name__)
        log.debug('hello,world~')
        log.info('python logs package.')
        log.warning('do not touch it!')
        log.error('runtime error!!')
        log.critical('out of memory!!!')

    def test_get_logger(self):
        log = Log(target='console').get_logger('TEST')
        log.debug('hello,world')
