#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    s = Student()
    s.name = 'Michael'
    s.age = 25
    # s.score = 99
