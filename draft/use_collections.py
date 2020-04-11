#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque


def test_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print('p:', p)
    print('isinstance(p, Point):', isinstance(p, Point))
    print('isinstance(p, tuple):', isinstance(p, tuple))


def test_deque():
    q = deque(['A', 'B', 'C'])
    q.append('X')
    q.appendleft('Y')
    print('q:', q)


if __name__ == '__main__':
    test_namedtuple()
    test_deque()
