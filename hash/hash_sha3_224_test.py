#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha3_224 import hash_sha3_224_encode, hash_sha3_224_check


class TestHashSHA3224(unittest.TestCase):
    def test_hash_sha3_224_encode(self):
        s = 'hello,world!'
        r = hash_sha3_224_encode(s)
        print('hash sha3_224 encode:', r)

    def test_hash_sha3_224_check(self):
        s = 'hello,world!'
        r = 'be93af91ae2dd882018a39e0769933340315aff480d880fe71913177'
        self.assertTrue(hash_sha3_224_check(s, r))
        print('hash sha3_224 check pass')
