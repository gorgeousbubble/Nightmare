#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import concurrent.futures as futures
import time
from socket import *


class TcpServer:
    def __init__(self, host='', port=6000):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.Clients = []
        self.Executor = futures.ThreadPoolExecutor(max_workers=3)
        self.Socket = socket(AF_INET, SOCK_STREAM)

    def start(self):
        try:
            print('Start Tcp Server')
            print('Listen Tcp:{}'.format(self.Addr))
            self.Socket.bind(self.Addr)
            self.Socket.listen(5)
        except Exception as e:
            print('Error listen Tcp:', e)
            exit(1)
        while True:
            try:
                print('Loop waiting for connect...')
                sock, addr = self.Socket.accept()
                self.Executor.submit(self.recv, sock, addr)
                print('Success accept client:{}'.format(addr))
                self.Clients.append((sock, addr))
            except Exception as e:
                print('Except break:', e)
                break

    def recv(self, sock, addr):
        try:
            while True:
                data = sock.recv(self.BufSize)
                if data:
                    print('[{}:{}] {}'.format(addr[0], addr[1], time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                    print('Remote->Local:{}'.format(data.decode('utf-8')))
                    for v in self.Clients:
                        if v[0] == sock:
                            print('[{}:{}] {}'.format(self.Addr[0], str(self.Addr[1]), time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                            print('Local->Remote:{}'.format(data.decode('utf-8')))
                            info = '{}'.format(data.decode('utf-8'))
                            v[0].send(info.encode('utf-8'))
                else:
                    break
        finally:
            print('Remote host forcibly closed connect:{}'.format(addr))
            self.Clients.remove((sock, addr))
            sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch tcp server listen, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch tcp server listen, such as \'6000\'', type=int, default=6000)
    args = parser.parse_args()
    s = TcpServer(host=args.ip, port=args.port)
    s.start()
