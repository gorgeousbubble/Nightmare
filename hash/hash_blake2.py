#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_blake2b(s):
    blake2b = hashlib.blake2b(digest_size=16)
    blake2b.update(s.encode('utf-8'))
    return blake2b.hexdigest()


def hash_blake2b_encode(s):
    blake2b = hashlib.blake2b(digest_size=16)
    blake2b.update(s.encode('utf-8'))
    return blake2b.hexdigest()


def hash_blake2b_check(s, r):
    blake2b = hashlib.blake2b(digest_size=16)
    blake2b.update(s.encode('utf-8'))
    return blake2b.hexdigest() == r
