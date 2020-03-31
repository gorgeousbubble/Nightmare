#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # string code part
    print('string code:')
    print("ord('A'):", ord('A'))
    print("chr(66):", chr(66))
    print("'ABC'.encode('ascii'):", 'ABC'.encode('ascii'))
    print("'ABC'.encode('utf-8'):", 'ABC'.encode('utf-8'))
    print("b'ABC'.decode('ascii'):", b'ABC'.decode('ascii'))
    print("b'ABC'.decode('utf-8'):", b'ABC'.decode('utf-8'))
    print("len(b'ABC'):", len(b'ABC'))
    print('')
    # string combine part
    print('string combine:')
    print("'hello,%s'%'world!':", 'hello,%s' % 'world!')
    print("'hi %s, you have $%d in bank.' % ('alopex', 100000000):",'hi %s, you have $%d in bank.' % ('alopex', 100000000))
    print('Today is %04d-%02d-%02d, time now: %2d:%02d pi is %f, symbol %%' % (2020, 2, 24, 3, 9, 3.1415926))
    print('We can also use \'format\' function to format str like this:', 'nice to meet you! {}'.format('erika'))
