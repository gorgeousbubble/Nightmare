#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    count = 0

    def __init__(self, name, score, gender='male'):
        self.__name = name
        self.__score = score
        self.__gender = gender
        Student.count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def set_gender(self, gender):
        self.__gender = gender

    def print_score(self):
        print('%s:%d' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    lisa = Student('Lisa', 99)
    print('create student lisa.')
    print('student count:', lisa.count)
    bart = Student('Bart', 59)
    print('create student bart.')
    print('student count:', bart.count)
    print(lisa.get_name(), lisa.get_grade())
    print(bart.get_name(), bart.get_grade())

