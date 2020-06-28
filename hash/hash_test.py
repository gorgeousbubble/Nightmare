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

    def test_hash_shake256_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'shake256')
        print('hash shake256 encode:', r)

    def test_hash_shake256_check(self):
        s = 'hello,world!'
        r = 'de9c5223df66f54d8ec0a07d36c5aa8ffbb9ed62b40050e476690cd99f41c23fbae714a5167bc48198d332d3c8c09beb4a8' \
            'b95fb37397d56f859b4242671b34536f76f84bc79cebed2cdb1b6458f2930d1d75920ff4121382525108d717cc7e4d158e3' \
            '5c0b558050bc28693edeceac8ca2041b469d4ac888b873b4363c4c816e03c36ad3e31ef88e5b3a618ad3aa7efe8c899687f' \
            'cbf5b7ef2985d62bf0779a1ef657ce43fd8ddaca4fb35aa9d45bd7242ecb272bf8b4bfd491fc61604eff58a5ecebb11c3be' \
            'c4a880f16be65544a6d2784124a2681cb1a9254f1c6495b984419db4caad8de452f95c1132b42d43819e1aaa45fb40e12e2' \
            '9a438205fdf018bc7'
        self.assertTrue(hash_check(s, r, 'shake256'))
        print('hash shake256 check pass')

    def test_hash_sha3_224_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha3_224')
        print('hash sha3_224 encode:', r)

    def test_hash_sha3_224_check(self):
        s = 'hello,world!'
        r = 'be93af91ae2dd882018a39e0769933340315aff480d880fe71913177'
        self.assertTrue(hash_check(s, r, 'sha3_224'))
        print('hash sha3_224 check pass')

    def test_hash_sha3_256_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha3_256')
        print('hash sha3_256 encode:', r)

    def test_hash_sha3_256_check(self):
        s = 'hello,world!'
        r = 'a2d2e46e20c995e295fadc00839288d74dd85b8feef8b778042427ab8ff6a5c5'
        self.assertTrue(hash_check(s, r, 'sha3_256'))
        print('hash sha3_256 check pass')

    def test_hash_sha3_384_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha3_384')
        print('hash sha3_384 encode:', r)

    def test_hash_sha3_384_check(self):
        s = 'hello,world!'
        r = '9f08f572fda8977e6a16abf5460a631fcd91d7f669efab1c9654afff28d2d52b230ca9189cd117d37ed0cfc2cb4c9223'
        self.assertTrue(hash_check(s, r, 'sha3_384'))
        print('hash sha3_512 check pass')

    def test_hash_sha3_512_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha3_512')
        print('hash sha3_384 encode:', r)

    def test_hash_sha3_512_check(self):
        s = 'hello,world!'
        r = '4ed8dc6739e8edaa481d548e7f93d7a6c63d833a75bcfbd615fd932c97e6f357316e10d488778b12d2b2004341b641c5' \
            '4fa3a7942555bdcc1f672c3bfa578725'
        self.assertTrue(hash_check(s, r, 'sha3_512'))
        print('hash sha3_512 check pass')

    def test_hash_hmac_md5_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'hmac_md5')
        print('hash hmac_md5 encode:', r)

    def test_hash_hmac_md5_check(self):
        s = 'hello,world!'
        r = '2db9a138d9070e0fda961ce2433fd44a'
        self.assertTrue(hash_check(s, r, 'hmac_md5'))
        print('hash hmac_md5 check pass')

    def test_hash_hmac_sha1_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'hmac_sha1')
        print('hash hmac_sha1 encode:', r)

    def test_hash_hmac_sha1_check(self):
        s = 'hello,world!'
        r = '97f4bedc9c92ac01026407d0dd04e3afd682e519'
        self.assertTrue(hash_check(s, r, 'hmac_sha1'))
        print('hash hmac_sha1 check pass')


if __name__ == '__main__':
    unittest.main()
