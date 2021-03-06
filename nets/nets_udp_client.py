#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import time
import threading
from socket import *


class UdpClient(object):
    def __init__(self, host='127.0.0.1', port=6001):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.Socket = socket(AF_INET, SOCK_DGRAM)

    def start(self):
        try:
            print('Start Udp Client')
            print('(Press Ctrl + Break to exit abort...)')
            t = threading.Thread(target=self.recv)
            t.setDaemon(True)
            t.start()
            while True:
                data = input()
                if not data:
                    break

                self.Socket.sendto(data.encode('utf-8'), self.Addr)
                print('[{}:{}] {}'.format(self.Addr[0], self.Addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Local->Remote:{}'.format(data))
        except Exception as e:
            print('Error send messages:', e)
        finally:
            self.Socket.close()

    def stop(self):
        self.Socket.close()
        print('Stop Udp Client')

    def recv(self):
        self.Socket.sendto('hello'.encode('utf-8'), self.Addr)
        while True:
            data, addr = self.Socket.recvfrom(self.BufSize)
            if not data:
                break
            print('[{}:{}] {}'.format(addr[0], str(addr[1]), time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            print('Remote->Client:{}'.format(data.decode('utf-8')))


def start_udp_client(host, port):
    c = UdpClient(host=host, port=port)
    c.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch tcp server listen, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch tcp server listen, such as \'6001\'', type=int, default=6001)
    args = parser.parse_args()
    start_udp_client(host=args.ip, port=args.port)
