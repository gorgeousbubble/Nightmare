#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return  n % 2 == 0


def not_empty(s):
    return s and s.strip()


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    i = _odd_iter()
    while True:
        n = next(i)
        yield n


def prime_gen(n):
    for i in range(2, n):
        b = True
        if i == 2:
            yield i
            continue
        for j in range(2, i):
            if i % j == 0:
                b = False
                break
        if b:
            yield i


def prime(n):
    l = []
    for i in prime_gen(n):
        l.append(i)
    return l


if __name__ == "__main__":
    print('test filter:')
    print('list(filter(is_odd, range(1, 11))):', list(filter(is_odd, range(1, 11))))
    print('list(filter(is_even, range(1, 11))):', list(filter(is_even, range(1, 11))))
    print('list(filter(not_empty, [\'A\', \'\', \'B\', None, \'C\', \'  \'])):', list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
    print('prime(100):', prime(100))
