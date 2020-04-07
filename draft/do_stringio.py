#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO


def test_string_io():
    f = StringIO()
    f.write('hello,')
    f.write('world!')
    print(f.getvalue())


def test_bytes_io():
    f = BytesIO()
    f.write(b'hello,')
    f.write(b'world!')
    print(f.getvalue())


if __name__ == '__main__':
    test_string_io()
    test_bytes_io()
