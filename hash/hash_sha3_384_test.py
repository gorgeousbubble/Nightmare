#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha3_384 import hash_sha3_384_encode, hash_sha3_384_check


class TestHashSHA3384(unittest.TestCase):
    def test_hash_sha3_384_encode(self):
        s = 'hello,world!'
        r = hash_sha3_384_encode(s)
        print('hash sha3_384 encode:', r)

    def test_hash_sha3_384_check(self):
        s = 'hello,world!'
        r = '9f08f572fda8977e6a16abf5460a631fcd91d7f669efab1c9654afff28d2d52b230ca9189cd117d37ed0cfc2cb4c9223'
        self.assertTrue(hash_sha3_384_check(s, r))
        print('hash sha3_384 check pass')


if __name__ == '__main__':
    unittest.main()
