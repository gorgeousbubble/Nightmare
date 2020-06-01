#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash import hash_gen, hash_check


class TestHash(unittest.TestCase):
    def test_hash_md5_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'md5')
        print('hash md5 encode:', r)

    def test_hash_md5_check(self):
        s = 'hello,world!'
        r = 'c0e84e870874dd37ed0d164c7986f03a'
        self.assertTrue(hash_check(s, r, 'md5'))
        print('hash md5 check pass')
