#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable


def iter_dict(**kwargs):
    print('iter_dict function:')
    print('iter1->')
    for i in kwargs.keys():
        print('{}:{}'.format(i, kwargs[i]))
    print()
    print('iter2->')
    for i in kwargs:
        print('{}:{}'.format(i, kwargs[i]))
    print()
    print('iter3->')
    for v in kwargs.values():
        print('{}'.format(v))
    print()
    print('iter4->')
    for k, v in kwargs.items():
        print('{}:{}'.format(k, v))
    print()
    print('iter5->')
    for _, v in kwargs.items():
        print('{}'.format(v))
    print()
    print('iter6->')
    for k, _ in kwargs.items():
        print('{}'.format(k))
    print()


def iter_list(*args):
    print('iter_list function:')
    print('list1->')
    for v in args:
        print('args[{}]:{}'.format(args.index(v), v))
    print()
    print('list2->')
    for k, v in enumerate(args):
        print('args[{}]:{}'.format(k, v))
    print()
    print('list3->')
    for v in iter(args):
        print('args[{}]:{}'.format(args.index(v), v))
    print()
    print('list4->')
    for k in range(len(args)):
        print('args[{}]:{}'.format(k, args[k]))
    print()


def find_min_and_max(L):
    if not isinstance(L, Iterable):
        raise TypeError('L should be iterable')
    if len(L) == 0:
        return None, None
    b = L[0]
    s = L[0]
    for v in L:
        if v > b:
            b = v
        if v < s:
            s = v
    return s, b


if __name__ == '__main__':
    dic = {'a': 1, 'b': 2, 'c': 3}
    lis = ['A', 'B', 'C', 'D', 'E']
    iter_dict(**dic)
    iter_list(*lis)
    # check iterable
    print('isinstance(dic, Iterable):', isinstance(dic, Iterable))
    print('isinstance(lis, Iterable):', isinstance(lis, Iterable))
    print('isinstance(\'ABC\', Iterable):', isinstance('ABC', Iterable))
    print('isinstance(123, Iterable):', isinstance(123, Iterable))
