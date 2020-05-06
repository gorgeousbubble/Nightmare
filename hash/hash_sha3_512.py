#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_512(s):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(s.encode('utf-8'))
    return sha3_512.hexdigest()
