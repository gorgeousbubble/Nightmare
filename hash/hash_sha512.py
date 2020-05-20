#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha512(s):
    sha512 = hashlib.sha512()
    sha512.update(s.encode('utf-8'))
    return sha512.hexdigest()


def hash_sha512_encode(s):
    sha512 = hashlib.sha512()
    sha512.update(s.encode('utf-8'))
    return sha512.hexdigest()


def hash_sha512_check(s, r):
    sha512 = hashlib.sha512()
    sha512.update(s.encode('utf-8'))
    return sha512.hexdigest() == r
