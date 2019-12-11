#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import datetime
import os
from logging.handlers import RotatingFileHandler


class Log(object):
    def __init__(self, target='console'):
        self.Target = target
        self.Level = logging.DEBUG
        self.Format = '%(asctime)s -%(levelname)s- [%(threadName)s:%(thread)d] (%(name)s:%(lineno)s) %(message)s'
        self.Logger = self.get_logger('__main__')
        # logs type console
        if self.Target == 'console':
            logging.basicConfig(level=self.Level, format=self.Format,
                                datefmt='%Y-%m-%d %H:%M:%S')
        # logs type file
        elif self.Target == 'file':
            if not os.path.exists('./log'):
                os.mkdir('./log')
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            name = './log/Nightmare_{}.log'.format(now)
            handler = logging.FileHandler(filename=name, encoding='utf-8', mode='a')
            logging.basicConfig(level=self.Level, format=self.Format,
                                datefmt='%Y-%m-%d %H:%M:%S', handlers=[handler])
        # logs type rotating files
        elif self.Target == 'rotating':
            if not os.path.exists('./log'):
                os.mkdir('./log')
            name = './log/Nightmare.log'
            handler = RotatingFileHandler(filename=name, maxBytes=4*1024*1024, backupCount=5)
            logging.basicConfig(level=self.Level, format=self.Format,
                                datefmt='%Y-%m-%d %H:%M:%S', handlers=[handler])
        # invalid logs type
        else:
            print('invalid logs type')

    def add_handler_stream(self):
        logger = self.Logger
        handler = logging.StreamHandler()
        handler.setLevel(self.Level)
        logger.addHandler(handler)

    def add_handler_file(self):
        if not os.path.exists('./log'):
            os.mkdir('./log')
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        name = './log/Nightmare_{}.log'.format(now)
        logger = self.Logger
        handler = logging.FileHandler(filename=name, encoding='utf-8', mode='a')
        handler.setLevel(self.Level)
        logger.addHandler(handler)

    def add_handler_rotating(self):
        if not os.path.exists('./log'):
            os.mkdir('./log')
        name = './log/Nightmare.log'
        logger = self.Logger
        handler = RotatingFileHandler(filename=name, maxBytes=4 * 1024 * 1024, backupCount=5)
        handler.setLevel(self.Level)
        logger.addHandler(handler)

    def get_logger_master(self):
        return self.Logger

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name=name)
        return logger


if __name__ == '__main__':
    log = Log(target='rotating').get_logger(__name__)
    log.debug('hello,world~')
    log.info('python logs package.')
    log.warning('do not touch it!')
    log.error('runtime error!!')
    log.critical('out of memory!!!')
    log.fatal('...')