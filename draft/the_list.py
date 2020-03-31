#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def iter_list(l):
    print('iter list:')
    for i, v in enumerate(l):
        print('list[{}]:{}'.format(i, v))


if __name__ == '__main__':
    classmates = ['Michael', 'Bob', 'Tracy']
    # original list content
    print('original list:')
    print('classmates:', classmates)
    print('len(classmates):', len(classmates))
    print('classmates[0]:', classmates[0])
    print('classmates[1]:', classmates[1])
    print('classmates[2]:', classmates[2])
    print('classmates[-1]:', classmates[-1])
    print('classmates[-2]:', classmates[-2])
    print('classmates[-3]:', classmates[-3])
    print('')
    # iterating list
    print('iterating list:')
    print('iter1->')
    for v in classmates:
        print('classmates[%d]:%s' % (classmates.index(v), v))
    print('iter2->')
    for i, v in enumerate(classmates):
        print('classmates[{}]:{}'.format(i, v))
    print('iter3->')
    for i in range(len(classmates)):
        print('classmates[{}]:{}'.format(i, classmates[i]))
    print('iter4->')
    for v in iter(classmates):
        print('classmates[%d]:%s' % (classmates.index(v), v))
    print('')
    # operate list
    print('operate list:')
    print('list append: Adam')
    classmates.append('Adam')
    iter_list(classmates)
    print('')
    print('list insert: 1, Jack')
    classmates.insert(1, 'Jack')
    iter_list(classmates)
    print('')
    print('list pop:')
    classmates.pop()
    iter_list(classmates)
    print('')
    print('list pop:1')
    classmates.pop(1)
    iter_list(classmates)
    print('')
    print('list element change:')
    classmates[1] = 'Sarah'
    iter_list(classmates)
    print('')
