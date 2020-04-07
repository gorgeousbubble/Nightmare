#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


if __name__ == '__main__':
    d = dict(name='Bob', age=20, score=88)
    j = json.dumps(d)
    print(d)
    print(j)
