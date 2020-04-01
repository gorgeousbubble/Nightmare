#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import functools


def lazy_sum(*args):
    def sum():
        s = 0
        for i in args:
            s += i
        return s
    return sum


def build(x, y):
    return lambda: x * x + y * y


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('execute')
def now():
    print(time.time())


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        r = func(*args, **kwargs)
        t_now = time.time()
        t_delta = t_now - t_start
        print('function cost time:', t_delta)
        return r
    return wrapper


@metric
def test_metric():
    time.sleep(3)


if __name__ == '__main__':
    f = lazy_sum(1, 2, 3, 4, 5)
    print('f:', f)
    print('f():', f())
    print(list(map(lambda x: x * x, range(1, 11))))
    print(list(filter(lambda x: x % 2 == 1, range(1, 20))))
    print('build(2, 3):', build(2, 3))
    now()
    print(now.__name__)
    print('start test metric function:')
    test_metric()
