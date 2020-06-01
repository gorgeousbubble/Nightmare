#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hash.hash_md5 import hash_md5, hash_md5_check
from hash.hash_sha1 import hash_sha1, hash_sha1_check
from hash.hash_sha224 import hash_sha224, hash_sha224_check
from hash.hash_sha256 import hash_sha256, hash_sha256_check
from hash.hash_sha384 import hash_sha384, hash_sha384_check
from hash.hash_sha512 import hash_sha512, hash_sha512_check
from hash.hash_sha3_224 import hash_sha3_224, hash_sha3_224_check
from hash.hash_sha3_256 import hash_sha3_256, hash_sha3_256_check
from hash.hash_sha3_384 import hash_sha3_384, hash_sha3_384_check
from hash.hash_sha3_512 import hash_sha3_512, hash_sha3_512_check
from hash.hash_shake import hash_shake128, hash_shake256, hash_shake128_check, hash_shake256_check
from hash.hash_blake2 import hash_blake2b, hash_blake2s, hash_blake2b_check, hash_blake2s_check


def hash_gen(s, t):
    # check input string
    if s == '':
        print('The input string can not be empty!')
        return
    # choose hash algorithm mode
    if t == 'md5':
        r = hash_md5(s)
        print('calc md5:{}'.format(r))
    elif t == 'sha1':
        r = hash_sha1(s)
        print('calc sha1:{}'.format(r))
    elif t == 'sha224':
        r = hash_sha224(s)
        print('calc sha224:{}'.format(r))
    elif t == 'sha256':
        r = hash_sha256(s)
        print('calc sha256:{}'.format(r))
    elif t == 'sha384':
        r = hash_sha384(s)
        print('calc sha384:{}'.format(r))
    elif t == 'sha512':
        r = hash_sha512(s)
        print('calc sha512:{}'.format(r))
    elif t == 'sha3_224':
        r = hash_sha3_224(s)
        print('calc sha3_224:{}'.format(r))
    elif t == 'sha3_256':
        r = hash_sha3_256(s)
        print('calc sha3_256:{}'.format(r))
    elif t == 'sha3_384':
        r = hash_sha3_384(s)
        print('calc sha3_384:{}'.format(r))
    elif t == 'sha3_512':
        r = hash_sha3_512(s)
        print('calc sha3_512:{}'.format(r))
    elif t == 'shake128':
        r = hash_shake128(s)
        print('calc shake128:{}'.format(r))
    elif t == 'shake256':
        r = hash_shake256(s)
        print('calc shake256:{}'.format(r))
    elif t == 'blake2b':
        r = hash_blake2b(s)
        print('calc blake2b:{}'.format(r))
    elif t == 'blake2s':
        r = hash_blake2s(s)
        print('calc blake2s:{}'.format(r))
    else:
        print('Invalid hash algorithm. You can choose one of hash algorithm from support list.')


def hash_check(s, r, t):
    # choose hash algorithm mode
    b = False
    if t == 'md5':
        b = hash_md5_check(s, r)
        print('check md5:{}'.format(b))
        return b
    elif t == 'sha1':
        b = hash_sha1_check(s, r)
        print('check sha1:{}'.format(b))
        return b
    elif t == 'sha224':
        b = hash_sha224_check(s, r)
        print('check sha224:{}'.format(b))
        return b
    elif t == 'sha256':
        b = hash_sha256_check(s, r)
        print('check sha256:{}'.format(b))
        return b
    elif t == 'sha384':
        b = hash_sha384_check(s, r)
        print('check sha384:{}'.format(b))
        return b
    elif t == 'sha512':
        b = hash_sha512_check(s, r)
        print('check sha512:{}'.format(b))
        return b
    elif t == 'sha3_224':
        b = hash_sha3_224_check(s, r)
        print('check sha3_224:{}'.format(b))
        return b
    elif t == 'sha3_256':
        b = hash_sha3_256_check(s, r)
        print('check sha3_256:{}'.format(b))
        return b
    elif t == 'sha3_384':
        b = hash_sha3_384_check(s, r)
        print('check sha3_384:{}'.format(b))
        return b
    elif t == 'sha3_512':
        b = hash_sha3_512_check(s, r)
        print('check sha3_512:{}'.format(b))
        return b
    elif t == 'shake128':
        b = hash_shake128_check(s, r)
        print('check shake128:{}'.format(b))
        return b
    elif t == 'shake256':
        b = hash_shake256_check(s, r)
        print('check shake256:{}'.format(b))
        return b
    elif t == 'blake2b':
        b = hash_blake2b_check(s, r)
        print('check blake2b:{}'.format(b))
        return b
    elif t == 'blake2s':
        b = hash_blake2s_check(s, r)
        print('check blake2s:{}'.format(b))
        return b
    else:
        print('Invalid hash algorithm. You can choose one of hash algorithm from support list.')
        return b
