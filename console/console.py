#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import functools
from enum import Enum


class ConsoleLevel(Enum):
    DEBUG = 0
    INFO = 1
    EVENT = 2
    WARN = 3
    ERROR = 4
    CRITICAL = 5


class Console(object):
    lock = threading.Lock()
    enable = True
    level = ConsoleLevel.DEBUG

    def thread_safe(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            Console.lock.acquire()
            ret = func(*args, **kwargs)
            Console.lock.release()
            return ret
        return wrapper

    @thread_safe
    def debug(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.DEBUG >= Console.level:
            print('[debug]->', end='')
            print(*args, **kwargs, flush=True)

    @thread_safe
    def info(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.INFO >= Console.level:
            print('[info]->', end='')
            print(*args, **kwargs, flush=True)

    @thread_safe
    def event(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.EVENT >= Console.level:
            print('[event]->', end='')
            print(*args, **kwargs, flush=True)

    @thread_safe
    def warn(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.WARN >= Console.level:
            print('[warning]->', end='')
            print(*args, **kwargs, flush=True)

    @thread_safe
    def error(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.ERROR >= Console.level:
            print('[error]->', end='')
            print(*args, **kwargs, flush=True)

    @thread_safe
    def critical(*args, **kwargs):
        if Console.enable is True and ConsoleLevel.CRITICAL >= Console.level:
            print('[critical]->', end='')
            print(*args, **kwargs, flush=True)
