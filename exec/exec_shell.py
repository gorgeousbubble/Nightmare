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


if __name__ == '__main__':
    exitcode, stdout, stderr = exec_shell('ls -al', timeout=5)
    if exitcode is None:
        print('execution timeout')
    elif exitcode != 0:
        print('error execute command \'ls -al\':{}'.format(stderr))
    else:
        print('success execute command \'ls -al\':{}'.format(stdout))
