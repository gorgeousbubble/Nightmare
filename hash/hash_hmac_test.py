#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_hmac import hash_hmac_md5_encode


class TestHashHMAC(unittest.TestCase):
    def test_hash_hmac_md5_encode(self):
        s = 'hello,world!'
        r = hash_hmac_md5_encode(s, '')
        print('hash hmac md5 encode:', r)


if __name__ == '__main__':
    unittest.main()
