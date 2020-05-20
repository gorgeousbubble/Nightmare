#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha256 import hash_sha256_encode, hash_sha256_check


class TestHashSHA256(unittest.TestCase):
    def test_hash_sha256_encode(self):
        s = 'hello,world!'
        r = hash_sha256_encode(s)
        print('hash sha256 encode:', r)

    def test_hash_sha256_check(self):
        s = 'hello,world!'
        r = 'ec1e0bd875226943ad0e8877bdba4ca449c4cb8591a5363921c9f1ee20084c34'
        self.assertTrue(hash_sha256_check(s, r))
        print('hash sha256 check pass')
