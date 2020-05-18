#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_256(s):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(s.encode('utf-8'))
    return sha3_256.hexdigest()


def hash_sha3_256_encode(s):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(s.encode('utf-8'))
    return sha3_256.hexdigest()


def hash_sha3_256_check(s, r):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(s.encode('utf-8'))
    return sha3_256.hexdigest() == r
