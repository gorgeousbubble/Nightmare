#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha224(s):
    sha224 = hashlib.sha224()
    sha224.update(s.encode('utf-8'))
    return sha224.hexdigest()


def hash_sha224_encode(s):
    sha224 = hashlib.sha224()
    sha224.update(s.encode('utf-8'))
    return sha224.hexdigest()


def hash_sha224_check(s, r):
    sha224 = hashlib.sha224()
    sha224.update(s.encode('utf-8'))
    return sha224.hexdigest() == r
