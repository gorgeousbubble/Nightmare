#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_sha1(s):
    sha1 = hashlib.sha1()
    sha1.update(s.encode('utf-8'))
    return sha1.hexdigest()
