#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def square_gen(n):
    if not isinstance(n, int):
        raise TypeError('illegal input type')
    if n <= 1:
        raise ValueError('illegal input range should more than 1')
    g = (i * i for i in range(1, n + 1))
    for i in g:
        print(i)


def fib(n):
    i, a, b = 0, 1, 1
    while i < n:
        yield b
        a, b = b, a + b
        i += 1
    return 'done'


def fib_gen(n):
    if not isinstance(n, int):
        raise TypeError('illegal input type')
    if n <= 2:
        raise ValueError('illegal input range should more than 2')
    for i in fib(n):
        print(i)


if __name__ == '__main__':
    print('generate square number:')
    square_gen(10)
    print('generate fibonacci number:')
    fib_gen(10)
