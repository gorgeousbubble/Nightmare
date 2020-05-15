#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_224(s):
    sha3_224 = hashlib.sha3_224()
    sha3_224.update(s.encode('utf-8'))
    return sha3_224.hexdigest()


def hash_sha3_224_encode(s):
    sha3_224 = hashlib.sha3_224()
    sha3_224.update(s.encode('utf-8'))
    return sha3_224.hexdigest()


def hash_sha3_224_check(s, r):
    sha3_224 = hashlib.sha3_224()
    sha3_224.update(s.encode('utf-8'))
    return sha3_224.hexdigest() == r
