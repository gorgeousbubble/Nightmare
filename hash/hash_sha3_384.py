#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_384(s):
    sha3_384 = hashlib.sha3_384()
    sha3_384.update(s.encode('utf-8'))
    return sha3_384.hexdigest()


def hash_sha3_384_encode(s):
    sha3_384 = hashlib.sha3_384()
    sha3_384.update(s.encode('utf-8'))
    return sha3_384.hexdigest()


def hash_sha3_384_check(s, r):
    sha3_384 = hashlib.sha3_384()
    sha3_384.update(s.encode('utf-8'))
    return sha3_384.hexdigest() == r
