#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def trim(s):
    # check parameter instance type
    if not isinstance(s, str):
        raise TypeError('error type of s')
    # calculate position of space
    if s == '':
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:len(s)-1])
    else:
        return s


if __name__ == '__main__':
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print("L:", L)
    # iterating list
    print('iterating list:')
    for k, v in enumerate(L):
        print('L[{}]:{}'.format(k, v))
    # slice of list'
    print('L[1:3]:', L[1:3])
    print('L[:2]:', L[:2])
    print('L[3:]:', L[3:])
    print('L[-2:]:', L[-2:])
