#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def move(x, y, step, arc):
    x = x + step * math.cos(arc)
    y = y - step * math.sin(arc)
    return x, y


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n -= 1
    return s


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


if __name__ == '__main__':
    print('test abs func:')
    print('my_abs(3):', my_abs(3))
    print('my_abs(-2):', my_abs(-2))
    print('test move func:')
    print('move(0, 0, 2, math.pi/6):', move(0, 0, 2, math.pi/6))
    print('quadratic(1, -5, 6):', quadratic(1, -5, 6))
    print('power(5):', power(5))
    print('power(2, 3):', power(2, 3))
    enroll('Sarah', 'F')
