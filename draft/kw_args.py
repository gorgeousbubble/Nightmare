#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def person(name, age, **kwargs):
    print(name, age, kwargs)


def product(*args):
    r = 1
    for v in args:
        r *= v
    return r


if __name__ == '__main__':
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    print('product(1, 2, 3):', product(1, 2, 3))
