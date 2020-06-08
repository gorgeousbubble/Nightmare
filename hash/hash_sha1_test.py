#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha1 import hash_sha1_encode, hash_sha1_check


class TestHashSHA1(unittest.TestCase):
    def test_hash_sha1_encode(self):
        s = 'hello,world!'
        r = hash_sha1_encode(s)
        print('hash sha1 encode:', r)

    def test_hash_sha1_check(self):
        s = 'hello,world!'
        r = '4518135c05e0706c0a34168996517bb3f28d94b5'
        self.assertTrue(hash_sha1_check(s, r))
        print('hash sha1 check pass')


if __name__ == '__main__':
    unittest.main()
