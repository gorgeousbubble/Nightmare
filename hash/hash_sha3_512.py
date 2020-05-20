#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_512(s):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(s.encode('utf-8'))
    return sha3_512.hexdigest()


def hash_sha3_512_encode(s):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(s.encode('utf-8'))
    return sha3_512.hexdigest()


def hash_sha3_512_check(s, r):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(s.encode('utf-8'))
    return sha3_512.hexdigest() == r
