#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64


def test_base64():
    s = b'hello,world!'
    print('s origin:', s)
    print('s encode:', base64.b64encode(s))
    print('s decode:', base64.b64decode(base64.b64encode(s)))


if __name__ == '__main__':
    test_base64()
