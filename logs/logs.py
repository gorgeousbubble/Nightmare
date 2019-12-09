#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import datetime
import os


class Logs(object):
    def __init__(self, target='console', level=logging.DEBUG):
        self.Target = target
        self.Level = level
        self.Format = '%(asctime)s %(levelname)s\t %(threadName)s %(name)s:%(lineno)s %(message)s'
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

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name=name)
        return logger


if __name__ == '__main__':
    logs = Logs(target='file').get_logger(__name__)
    logs.debug('hello,world~')
    logs.info('python logs package.')
    logs.warning('do not touch it!')