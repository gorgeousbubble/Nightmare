#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    # original dict content
    print('original dict content:')
    print(dic)
    print('')
    # iterating dict
    print('iterating dict:')
    print('iter1->')
    for k in dic.keys():
        print('name:%s, score:%d' % (k, dic[k]))
    print('')
    print('iter2->')
    for k, v in dic.items():
        print('name:%s, score:%d' % (k, v))
    print('')
    print('iter3->')
    for v in dic.values():
        print(v)
    print('')
    print('iter4->')
    for (k, v) in dic.items():
        print('dic[{}]:{}'.format(k, v))
    print('')
    # change the value of Michael
    dic['Michael'] = 90
    print(dic)
    print('')
