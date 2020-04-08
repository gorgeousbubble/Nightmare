#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
from .exec_shell import exec_shell
from .exec_cmd import exec_command


def exec(cmd, timeout=5):
    system = platform.system()
    if system == 'Windows':
        return exec_command(cmd, timeout)
    elif system == 'Linux':
        return exec_shell(cmd, timeout)
    else:
        return exec_shell(cmd, timeout)
