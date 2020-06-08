#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_md5 import hash_md5_encode, hash_md5_check


class TestHashMD5(unittest.TestCase):
    def test_hash_md5_encode(self):
        s = 'hello,world!'
        r = hash_md5_encode(s)
        print('hash md5 encode:', r)

    def test_hash_md5_check(self):
        s = 'hello,world!'
        r = 'c0e84e870874dd37ed0d164c7986f03a'
        self.assertTrue(hash_md5_check(s, r))
        print('hash md5 check pass')


if __name__ == '__main__':
    unittest.main()
