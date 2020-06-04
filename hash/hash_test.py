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

    def test_hash_sha512_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha512')
        print('hash sha512 encode:', r)

    def test_hash_sha512_check(self):
        s = 'hello,world!'
        r = 'fa9edcfdaab7a4165f8d2593f04077d46aca957493e7e181ca479582d519a299d96730' \
            '5294d5d46fb5e0158240441b94cd96510c2311bdc86870e5ebf3efe60c'
        self.assertTrue(hash_check(s, r, 'sha512'))
        print('hash sha512 check pass')

    def test_hash_blake2b_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'blake2b')
        print('hash blake2b encode:', r)

    def test_hash_blake2b_check(self):
        s = 'hello,world!'
        r = '1748e3d0f53508245851db4571424eee'
        self.assertTrue(hash_check(s, r, 'blake2b'))
        print('hash blake2b check pass')

    def test_hash_blake2s_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'blake2s')
        print('hash blake2s encode:', r)

    def test_hash_blake2s_check(self):
        s = 'hello,world!'
        r = 'fec96d2115ab677ca3e7561ce32100bd'
        self.assertTrue(hash_check(s, r, 'blake2s'))
        print('hash blake2s check pass')

    def test_hash_shake128_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'shake128')
        print('hash shake128 encode:', r)

    def test_hash_shake128_check(self):
        s = 'hello,world!'
        r = '12eaea2f1de368092b5418c6c5c8575a9a3490fd8d3c85a7fac818ccba01ea5d4526c2e6055b77b2b02a9b3b19f4b316dfc' \
            '2c667dc18eda5522148e2949df7a3b6a25f37c9935e784077985dc95930d210b9aae7fb6a1f0491d1077177db27bdce8ce0' \
            '3b5d5e7079abf4f30dd9aef53e518d4909e5421f8275ecb075e4de7543'
        self.assertTrue(hash_check(s, r, 'shake128'))
        print('hash shake128 check pass')


if __name__ == '__main__':
    unittest.main()
