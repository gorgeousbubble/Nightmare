#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime


def test_date():
    t = datetime.now()
    ts = t.timestamp()
    print('time now:{}'.format(t))
    print('timestamp:{}'.format(ts))


if __name__ == '__main__':
    test_date()
