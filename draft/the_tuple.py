#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def iter_tuple(l):
    print('iter tuple:')
    for i, v in enumerate(l):
        print('tuple[{}]:{}'.format(i, v))


if __name__ == '__main__':
    classmates = ('Michael', 'Bob', 'Tracy')
    # original tuple content
    print('original tuple:')
    print('classmates:', classmates)
    print('len(classmates):', len(classmates))
    print('classmates[0]:', classmates[0])
    print('classmates[1]:', classmates[1])
    print('classmates[2]:', classmates[2])
    print('classmates[-1]:', classmates[-1])
    print('classmates[-2]:', classmates[-2])
    print('classmates[-3]:', classmates[-3])
    print('')
    # iterating tuple
    print('iterating tuple:')
    iter_tuple(classmates)
    print('')
