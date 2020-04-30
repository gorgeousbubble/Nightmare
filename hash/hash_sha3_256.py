#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha3_256(s):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(s.encode('utf-8'))
    return sha3_256.hexdigest()
