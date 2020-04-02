#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return 'Student: name:{}, age:{}, gender:{}'.format(self.name, self.age, self.gender)


if __name__ == '__main__':
    day1 = Weekday.Mon
    print(day1)
    for name, member in Weekday.__members__.items():
        print(name, '=>', member)
    s = Student(name='Michael', age=12, gender=Gender.Male)
    print(s)
