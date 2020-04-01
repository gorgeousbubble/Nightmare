#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def by_name(p):
    name, score = p
    return name


if __name__ == '__main__':
    print('test sorted:')
    l = [36, 5, -12, 9, -21]
    print('original list:', l)
    print('sorted list:', sorted(l))
    print('sorted abs list:', sorted(l, key=abs))
    l = ['bob', 'about', 'Zoo', 'Credit']
    print('original list:', l)
    print('sorted list:', sorted(l))
    print('sorted low case list:', sorted(l, key=str.lower))
    print('sorted reserved list:', sorted(l, reverse=True))
    l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    l = sorted(l, key=by_name)
    print(l)
