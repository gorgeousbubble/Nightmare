#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def calc(*args):
    sum = 0
    for v in args:
        sum += math.pow(v, 2)
    return sum


if __name__ == '__main__':
    print('calc sum func:')
    print('calc(1, 2, 3):', calc(1, 2, 3))
    num = [1, 3, 5]
    print('calc(*num):', calc(*num))
