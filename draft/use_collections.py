#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple


def test_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print('p:', p)
    print('isinstance(p, Point):', isinstance(p, Point))
    print('isinstance(p, tuple):', isinstance(p, tuple))


if __name__ == '__main__':
    test_namedtuple()
