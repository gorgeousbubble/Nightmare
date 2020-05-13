#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha384(s):
    sha384 = hashlib.sha384()
    sha384.update(s.encode('utf-8'))
    return sha384.hexdigest()


def hash_sha384_encode(s):
    sha384 = hashlib.sha384()
    sha384.update(s.encode('utf-8'))
    return sha384.hexdigest()


def hash_sha384_check(s, r):
    sha384 = hashlib.sha384()
    sha384.update(s.encode('utf-8'))
    return sha384.hexdigest() == r
