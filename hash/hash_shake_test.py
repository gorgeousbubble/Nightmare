#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_shake import hash_shake128_encode, hash_shake128_check


class TestHashShake(unittest.TestCase):
    def test_hash_shake128_encode(self):
        s = 'hello,world!'
        r = hash_shake128_encode(s)
        print('hash shake128 encode:', r)

    def test_hash_shake128_check(self):
        s = 'hello,world!'
        r = '12eaea2f1de368092b5418c6c5c8575a9a3490fd8d3c85a7fac818ccba01ea5d4526c2e6055b77b2b02a9b3b19f4b316dfc' \
            '2c667dc18eda5522148e2949df7a3b6a25f37c9935e784077985dc95930d210b9aae7fb6a1f0491d1077177db27bdce8ce0' \
            '3b5d5e7079abf4f30dd9aef53e518d4909e5421f8275ecb075e4de7543'
        self.assertTrue(hash_shake128_check(s, r))
        print('hash shake128 check pass')
