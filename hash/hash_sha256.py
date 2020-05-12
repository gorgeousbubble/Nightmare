#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha256(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest()


def hash_sha256_encode(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest()


def hash_sha256_check(s, r):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest() == r
