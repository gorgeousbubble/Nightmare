#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import concurrent.futures as futures
import time
from socket import *


class TcpClient(object):
    def __init__(self, host='127.0.0.1', port=6000):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.Socket = socket(AF_INET, SOCK_STREAM)

    def start(self):
        try:
            print('Start Tcp Client')
            print('Connect to Tcp Server:{}'.format(self.Addr))
            self.Socket.connect(self.Addr)
            pass
        except Exception as e:
            print('Error connect to server:', e)
            self.stop()
            exit(1)

    def stop(self):
        self.Socket.close()
        print('Stop Tcp Client')

    def send(self, data):
        addr = self.Socket.getsockname()
        print('[{}:{}] {}'.format(addr[0], str(addr[1]), time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        print('Local->Remote:{}'.format(data))
        self.Socket.send(data.encode('utf-8'))

    def recv(self):
        try:
            while True:
                data = self.Socket.recv(self.BufSize)
                if not data:
                    break
                print('[{}:{}] {}'.format(self.Addr[0], str(self.Addr[1]), time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Remote->Local:{}'.format(data.decode('utf-8')))
        finally:
            print('Remote host forcibly closed connect:{}'.format(self.Addr))
            self.Socket.close()


def start_tcp_client(host, port):
    c = TcpClient(host=host, port=port)
    c.start()
    futures.ThreadPoolExecutor(max_workers=1).submit(c.recv)

    while True:
        try:
            data = input()
            if not data:
                c.Socket.close()
                break
            c.send(data)
        except Exception as e:
            c.Socket.close()
            print('Except break:', e)
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch tcp client connect, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch tcp client connect, such as \'6000\'', type=int, default=6000)
    args = parser.parse_args()
    start_tcp_client(host=args.ip, port=args.port)
