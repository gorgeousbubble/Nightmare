#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


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


def test_defaultdict():
    d = defaultdict(lambda: 'N/A')
    d['key1'] = 'abc'
    print('d[\'key1\']:', d['key1'])
    print('d[\'key2\']:', d['key2'])


def test_ordereddict():
    d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(d)


def test_counter():
    c = Counter()
    for ch in 'programming':
        c[ch] += 1
    print(c)


if __name__ == '__main__':
    test_namedtuple()
    test_deque()
    test_defaultdict()
    test_ordereddict()
    test_counter()
