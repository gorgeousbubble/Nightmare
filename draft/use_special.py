#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


if __name__ == '__main__':
    s = Student(name='Michael')
    print(s)
    print(s.age)
    for i in Fib():
        print(i)
