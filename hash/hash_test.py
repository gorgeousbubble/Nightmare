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

    def test_hash_sha1_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha1')
        print('hash sha1 encode:', r)

    def test_hash_sha1_check(self):
        s = 'hello,world!'
        r = '4518135c05e0706c0a34168996517bb3f28d94b5'
        self.assertTrue(hash_check(s, r, 'sha1'))
        print('hash sha1 check pass')

    def test_hash_sha224_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha224')
        print('hash sha224 encode:', r)

    def test_hash_sha224_check(self):
        s = 'hello,world!'
        r = '8ca8306359700b64b25a070da3c042dc8fa6a885427580d2b6d774f4'
        self.assertTrue(hash_check(s, r, 'sha224'))
        print('hash sha224 check pass')

    def test_hash_sha256_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha256')
        print('hash sha256 encode:', r)

    def test_hash_sha256_check(self):
        s = 'hello,world!'
        r = 'ec1e0bd875226943ad0e8877bdba4ca449c4cb8591a5363921c9f1ee20084c34'
        self.assertTrue(hash_check(s, r, 'sha256'))
        print('hash sha256 check pass')

    def test_hash_sha384_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha384')
        print('hash sha384 encode:', r)

    def test_hash_sha384_check(self):
        s = 'hello,world!'
        r = 'ceff8fdf21cc4e0f5217f7b674af88e5337636728d0d0b87acc28923a206d3a975443197253ceb306a3ff9b8e83f3c5a'
        self.assertTrue(hash_check(s, r, 'sha384'))
        print('hash sha384 check pass')


if __name__ == '__main__':
    unittest.main()
