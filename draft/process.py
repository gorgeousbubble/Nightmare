#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import random
from multiprocessing import Process
from multiprocessing import Pool


def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))


def start_proc():
    print('run parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child process will start...')
    p.start()
    p.join()
    print('child process end.')


def task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    t_start = time.time()
    time.sleep(random.random() * 3)
    t_end = time.time()
    print('task %s runs %0.2f seconds.' % (name, (t_end - t_start)))


def start_pool():
    pass


if __name__ == '__main__':
    pass
