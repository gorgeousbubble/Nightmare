#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha512 import hash_sha512_encode, hash_sha512_check


class TestHashSHA512(unittest.TestCase):
    def test_hash_sha512_encode(self):
        s = 'hello,world!'
        r = hash_sha512_encode(s)
        print('hash sha512 encode:', r)

    def test_hash_sha512_check(self):
        s = 'hello,world!'
        r = 'fa9edcfdaab7a4165f8d2593f04077d46aca957493e7e181ca479582d519a299d96730' \
            '5294d5d46fb5e0158240441b94cd96510c2311bdc86870e5ebf3efe60c'
        self.assertTrue(hash_sha512_check(s, r))
        print('hash sha512 check pass')
