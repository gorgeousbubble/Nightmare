#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hmac


def hash_hmac_md5(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5')
    return h.hexdigest()


def hash_hmac_md5_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5')
    return h.hexdigest()


def hash_hmac_md5_check(s, k, r):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5')
    return h.hexdigest() == r


def hash_hmac_sha1(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA1')
    return h.hexdigest()


def hash_hmac_sha1_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA1')
    return h.hexdigest()


def hash_hmac_sha1_check(s, k, r):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA1')
    return h.hexdigest() == r


def hash_hmac_sha256(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA256')
    return h.hexdigest()


def hash_hmac_sha256_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA256')
    return h.hexdigest()


def hash_hmac_sha256_check(s, k, r):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA256')
    return h.hexdigest() == r


def hash_hmac_sha512(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA512')
    return h.hexdigest()


def hash_hmac_sha512_encode(s, k):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA512')
    return h.hexdigest()


def hash_hmac_sha512_check(s, k, r):
    h = hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'SHA512')
    return h.hexdigest() == r
