#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha384 import hash_sha384_encode, hash_sha384_check


class TestHashSHA384(unittest.TestCase):
    def test_hash_sha384_encode(self):
        s = 'hello,world!'
        r = hash_sha384_encode(s)
        print('hash sha384 encode:', r)

    def test_hash_sha384_check(self):
        s = 'hello,world!'
        r = 'ceff8fdf21cc4e0f5217f7b674af88e5337636728d0d0b87acc28923a206d3a975443197253ceb306a3ff9b8e83f3c5a'
        self.assertTrue(hash_sha384_check(s, r))
        print('hash sha384 check pass')
