#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_sha3_512 import hash_sha3_512_encode, hash_sha3_512_check


class TestHashSHA3512(unittest.TestCase):
    def test_hash_sha3_512_encode(self):
        s = 'hello,world!'
        r = hash_sha3_512_encode(s)
        print('hash sha3_512 encode:', r)

    def test_hash_sha3_512_check(self):
        s = 'hello,world!'
        r = '4ed8dc6739e8edaa481d548e7f93d7a6c63d833a75bcfbd615fd932c97e6f357316e10d488778b12d2b2004341b641c54fa3a794' \
            '2555bdcc1f672c3bfa578725'
        self.assertTrue(hash_sha3_512_check(s, r))
        print('hash sha3_512 check pass')


if __name__ == '__main__':
    unittest.main()
