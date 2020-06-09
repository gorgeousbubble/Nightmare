#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha224 import hash_sha224_encode, hash_sha224_check


class TestHashSHA224(unittest.TestCase):
    def test_hash_sha224_encode(self):
        s = 'hello,world!'
        r = hash_sha224_encode(s)
        print('hash sha224 encode:', r)

    def test_hash_sha224_check(self):
        s = 'hello,world!'
        r = '8ca8306359700b64b25a070da3c042dc8fa6a885427580d2b6d774f4'
        self.assertTrue(hash_sha224_check(s, r))
        print('hash sha224 check pass')


if __name__ == '__main__':
    unittest.main()
