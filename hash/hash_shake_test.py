#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_shake import hash_shake128_encode, hash_shake128_check, hash_shake256_encode, hash_shake256_check


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

    def test_hash_shake256_encode(self):
        s = 'hello,world!'
        r = hash_shake256_encode(s)
        print('hash shake256 encode:', r)

    def test_hash_shake256_check(self):
        s = 'hello,world!'
        r = 'de9c5223df66f54d8ec0a07d36c5aa8ffbb9ed62b40050e476690cd99f41c23fbae714a5167bc48198d332d3c8c09beb4a8' \
            'b95fb37397d56f859b4242671b34536f76f84bc79cebed2cdb1b6458f2930d1d75920ff4121382525108d717cc7e4d158e3' \
            '5c0b558050bc28693edeceac8ca2041b469d4ac888b873b4363c4c816e03c36ad3e31ef88e5b3a618ad3aa7efe8c899687f' \
            'cbf5b7ef2985d62bf0779a1ef657ce43fd8ddaca4fb35aa9d45bd7242ecb272bf8b4bfd491fc61604eff58a5ecebb11c3be' \
            'c4a880f16be65544a6d2784124a2681cb1a9254f1c6495b984419db4caad8de452f95c1132b42d43819e1aaa45fb40e12e2' \
            '9a438205fdf018bc7'
        self.assertTrue(hash_shake256_check(s, r))
        print('hash shake256 check pass')
