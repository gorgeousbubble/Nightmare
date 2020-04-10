#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time


number = 0
lock = threading.Lock()


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)


def start_loop():
    print('start loop start...')
    t = threading.Thread(name='thread_loop', target=loop)
    t.start()
    t.join()
    print('start loop ended.')


def operate_once(n):
    global number
    with lock:
        number = number + n
        number = number - n


def run_thread(n):
    for i in range(100000):
        operate_once(n)


def start_lock():
    t1 = threading.Thread(name='thread_add', target=run_thread, args=(2,))
    t2 = threading.Thread(name='thread_sub', target=run_thread, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('number:%s' % number)


if __name__ == '__main__':
    start_lock()
