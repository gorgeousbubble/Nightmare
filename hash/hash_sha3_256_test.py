#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha3_256 import hash_sha3_256_encode, hash_sha3_256_check


class TestHashSHA3256(unittest.TestCase):
    def test_hash_sha3_256_encode(self):
        s = 'hello,world!'
        r = hash_sha3_256_encode(s)
        print('hash sha3_256 encode:', r)

    def test_hash_sha3_256_check(self):
        s = 'hello,world!'
        r = 'a2d2e46e20c995e295fadc00839288d74dd85b8feef8b778042427ab8ff6a5c5'
        self.assertTrue(hash_sha3_256_check(s, r))
        print('hash sha3_256 check pass')
