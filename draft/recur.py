#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if n < 0:
        raise ValueError('illegal parameter value')
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)


def fact_iter(n, p=1):
    if n < 0:
        raise ValueError('illegal parameter value')
    elif n == 0:
        return p
    else:
        return fact_iter(n-1, n*p)


if __name__ == '__main__':
    print('fact(5):', fact(5))
    print('fact_iter(12):', fact_iter(12))
