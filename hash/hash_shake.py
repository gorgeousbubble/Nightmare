#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_shake128(s):
    shake128 = hashlib.shake_128()
    shake128.update(s.encode('utf-8'))
    return shake128.hexdigest(128)


def hash_shake128_encode(s):
    shake128 = hashlib.shake_128()
    shake128.update(s.encode('utf-8'))
    return shake128.hexdigest(128)


def hash_shake128_check(s, r):
    shake128 = hashlib.shake_128()
    shake128.update(s.encode('utf-8'))
    return shake128.hexdigest(128) == r
