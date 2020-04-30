#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_384(s):
    sha3_384 = hashlib.sha3_384()
    sha3_384.update(s.encode('utf-8'))
    return sha3_384.hexdigest()
