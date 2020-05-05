#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha384(s):
    sha384 = hashlib.sha384()
    sha384.update(s.encode('utf-8'))
    return sha384.hexdigest()
