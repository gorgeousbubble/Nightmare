#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import time


def exec_shell(cmd, timeout=5):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    t_start = time.time()
    while True:
        if p.poll() is not None:
            break
        t_now = time.time()
        t_delta = t_now - t_start
        if t_delta > timeout:
            p.terminate()
            return None, None, None
        time.sleep(0.1)
    return p.returncode, p.stdout.read(), p.stderr.read()
