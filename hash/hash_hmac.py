#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hmac


def hash_hmac_md5_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5')
    return h.hexdigest()


def hash_hmac_sha1_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA1')
    return h.hexdigest()


def hash_hmac_sha256_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA256')
    return h.hexdigest()


def hash_hmac_sha512_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA512')
    return h.hexdigest()
