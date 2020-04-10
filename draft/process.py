#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import random
import subprocess
from multiprocessing import Process, Queue
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
    print('parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(4):
        p.apply_async(task, args=(i,))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocesses done.')


def start_sub():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('exitcode:{}'.format(r))


def write(q):
    print('process to write: %s' % os.getpid())
    for v in ['A', 'B', 'C']:
        print('put %s to queue...' % v)
        q.put(v)
        time.sleep(random.random())


def read(q):
    print('process to read: %s' % os.getpid())
    while True:
        v = q.get(True)
        print('get %s from queue...' % v)


def start_queue():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


if __name__ == '__main__':
    start_queue()
