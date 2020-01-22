#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import logging.config
import datetime
import yaml
import os
import os.path


class LogYaml(object):
    def __init__(self, file='./yaml/log.yaml', level=logging.DEBUG, path='./log', app='Nightmare'):
        self.file = file
        self.level = level
        self.path = path
        self.app = app
        # open the yaml configure file
        if os.path.exists(file):
            with open(file, 'r') as fd:
                conf = yaml.load(fd)
                logging.config.dictConfig(conf)
        else:
            logging.basicConfig(level=self.level)

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name=name)
        return logger


if __name__ == '__main__':
    log = LogYaml(file='./yaml/log.yaml', path='../log').get_logger(__name__)
    log.debug('hello,world~')
    log.info('python logs package.')
