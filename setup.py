#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from distutils.core import setup, Extension
from Cython.Build import cythonize


setup(
    ext_modules=cythonize(['main.py'], compiler_directives=dict(
        always_allow_keywords=True,
        c_string_encoding='utf-8',
        language_level=3,
    ))
)
