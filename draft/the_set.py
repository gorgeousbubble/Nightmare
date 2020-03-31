#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = set([1, 1, 2, 2, 2, 3, 3, 1, 2, 4, 3, 3, 4, 5])
    print('original set content:')
    print("s:", s)
    print()
    print('test add method:')
    s.add(7)
    print("s:", s)
    print()
    print('test remove method:')
    s.remove(7)
    print("s:", s)
    print()
