#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def square(i):
    return i * i


def append(i, j):
    return i + j


def normalize(name):
    if not isinstance(name, str):
        raise TypeError('illegal input type')
    return name.capitalize()


def test_map(L):
    return list(map(square, L))


def test_reduce(L):
    return reduce(append, L)


if __name__ == '__main__':
    print('test keyword:')
    print('test_map([1, 2, 3, 4, 5]):', test_map([1, 2, 3, 4, 5]))
    print('test_reduce(test_map([1, 2, 3, 4, 5])):', test_reduce(test_map([1, 2, 3, 4, 5])))
