#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    salary = input('please input your salary:')
    salary = int(salary)
    if salary < 1000:
        print('salary low')
    elif salary < 5000:
        print('salary mid')
    else:
        print('salary high')
