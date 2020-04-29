#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from hash.hash_md5 import hash_md5
from hash.hash_sha1 import hash_sha1
from hash.hash_sha224 import hash_sha224
from hash.hash_sha256 import hash_sha256
from hash.hash_sha384 import hash_sha384
from hash.hash_sha512 import hash_sha512
from hash.hash_sha3_224 import hash_sha3_224
from hash.hash_sha3_256 import hash_sha3_256


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
    else:
        print('Invalid hash algorithm. You can choose one of hash algorithm from support list.')
