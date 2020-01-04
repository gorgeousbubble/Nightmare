#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import datetime
import os
from logging.handlers import RotatingFileHandler


class Log(object):
    def __init__(self, target='console', level=logging.DEBUG, path='./log', app='Nightmare'):
        self.target = target
        self.level = level
        self.path = path
        self.app = app
        self.format = '%(asctime)s -%(levelname)s- [%(threadName)s:%(thread)d] (%(name)s:%(lineno)s) %(message)s'
        self.logger = self.get_logger('__main__')
        # logs type console
        if self.target == 'console':
            logging.basicConfig(level=self.level, format=self.format,
                                datefmt='%Y-%m-%d %H:%M:%S')
        # logs type file
        elif self.target == 'file':
            if not os.path.exists(path):
                os.mkdir(path)
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            name = os.path.join(path, '{}_{}.log'.format(app, now))
            handler = logging.FileHandler(filename=name, encoding='utf-8', mode='a')
            logging.basicConfig(level=self.level, format=self.format,
                                datefmt='%Y-%m-%d %H:%M:%S', handlers=[handler])
        # logs type rotating files
        elif self.target == 'rotating':
            if not os.path.exists(path):
                os.mkdir(path)
            name = os.path.join(path, '{}.log'.format(app))
            handler = RotatingFileHandler(filename=name, maxBytes=4*1024*1024, backupCount=5)
            logging.basicConfig(level=self.level, format=self.format,
                                datefmt='%Y-%m-%d %H:%M:%S', handlers=[handler])
        # invalid logs type
        else:
            print('invalid logs type')

    def add_handler_stream(self):
        logger = self.logger
        handler = logging.StreamHandler()
        handler.setLevel(self.level)
        logger.addHandler(handler)

    def add_handler_file(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        name = os.path.join(self.path, '{}_{}.log'.format(self.app, now))
        logger = self.logger
        handler = logging.FileHandler(filename=name, encoding='utf-8', mode='a')
        handler.setLevel(self.level)
        logger.addHandler(handler)

    def add_handler_rotating(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        name = os.path.join(self.path, '{}.log'.format(self.app))
        logger = self.logger
        handler = RotatingFileHandler(filename=name, maxBytes=4 * 1024 * 1024, backupCount=5)
        handler.setLevel(self.level)
        logger.addHandler(handler)

    def get_logger_master(self):
        return self.logger

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name=name)
        return logger


if __name__ == '__main__':
    log = Log(target='rotating', path='../log').get_logger(__name__)
    log.debug('hello,world~')
    log.info('python logs package.')
    log.warning('do not touch it!')
    log.error('runtime error!!')
    log.critical('out of memory!!!')
    log.fatal('...')