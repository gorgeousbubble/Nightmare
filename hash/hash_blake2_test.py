#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_blake2 import hash_blake2b_encode, hash_blake2b_check, hash_blake2s_encode, hash_blake2s_check


class TestHashBlake2(unittest.TestCase):
    def test_hash_blake2b_encode(self):
        s = 'hello,world!'
        r = hash_blake2b_encode(s)
        print('hash blake2b encode:', r)

    def test_hash_blake2b_check(self):
        s = 'hello,world!'
        r = '1748e3d0f53508245851db4571424eee'
        self.assertTrue(hash_blake2b_check(s, r))
        print('hash blake2b check pass')

    def test_hash_blake2s_encode(self):
        s = 'hello,world!'
        r = hash_blake2s_encode(s)
        print('hash blake2s encode:', r)

    def test_hash_blake2s_check(self):
        s = 'hello,world!'
        r = 'fec96d2115ab677ca3e7561ce32100bd'
        self.assertTrue(hash_blake2s_check(s, r))
        print('hash blake2s check pass')
