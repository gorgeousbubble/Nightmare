#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from .hash_hmac import hash_hmac_md5_encode, hash_hmac_sha1_encode, hash_hmac_sha256_encode, hash_hmac_sha512_encode,\
    hash_hmac_md5_check, hash_hmac_sha1_check, hash_hmac_sha256_check, hash_hmac_sha512_check


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

    def test_hash_hmac_sha1_check(self):
        s = 'hello,world!'
        r = '97f4bedc9c92ac01026407d0dd04e3afd682e519'
        self.assertTrue(hash_hmac_sha1_check(s, '', r))

    def test_hash_hmac_sha256_check(self):
        s = 'hello,world!'
        r = 'b3573c8ed2a62017f5503f06e78549fe1a55355c1e7e1f925bdb8f0b9c8a029f'
        self.assertTrue(hash_hmac_sha256_check(s, '', r))

    def test_hash_hmac_sha512_check(self):
        s = 'hello,world!'
        r = 'e80ef886694e53473de1e01e328e40dd20289e2f7a61f4a93b036259343ee02a7d5026dffa10847077f4e8486d7c1ce20b697c7c' \
            'e8d8decddf91bef3ff78f4c8'
        self.assertTrue(hash_hmac_sha512_check(s, '', r))


if __name__ == '__main__':
    unittest.main()
