#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_hmac import hash_hmac_md5_encode, hash_hmac_sha1_encode, hash_hmac_sha256_encode, hash_hmac_sha512_encode,\
    hash_hmac_md5_check


class TestHashHMAC(unittest.TestCase):
    def test_hash_hmac_md5_encode(self):
        s = 'hello,world!'
        r = hash_hmac_md5_encode(s, '')
        print('hash hmac md5 encode:', r)

    def test_hash_hmac_sha1_encode(self):
        s = 'hello,world!'
        r = hash_hmac_sha1_encode(s, '')
        print('hash hmac sha1 encode:', r)

    def test_hash_hmac_sha256_encode(self):
        s = 'hello,world!'
        r = hash_hmac_sha256_encode(s, '')
        print('hash hmac sha256 encode:', r)

    def test_hash_hmac_sha512_encode(self):
        s = 'hello,world!'
        r = hash_hmac_sha512_encode(s, '')
        print('hash hmac sha512 encode:', r)

    def test_hash_hmac_md5_check(self):
        s = 'hello,world!'
        r = '2db9a138d9070e0fda961ce2433fd44a'
        self.assertTrue(hash_hmac_md5_check(s, '', r))


if __name__ == '__main__':
    unittest.main()
