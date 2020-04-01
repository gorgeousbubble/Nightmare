#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test_list():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [i.lower() for i in L1 if isinstance(i, str)]
    print(L1)
    print(L2)


if __name__ == '__main__':
    print('list comprehensions:')
    print('range 1~10:', [i for i in range(1, 11)])
    print('square 1~10:', [i * i for i in range(1, 11)])
    print('square odd 1~10:', [i * i for i in range(1, 11) if i % 2 == 0])
    print('combine alpha:', [i + j for i in 'ABC' for j in 'XYZ'])
    test_list()
