#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import time
from socket import *


class UdpServer(object):
    def __init__(self, host='', port=6001):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.Socket = socket(AF_INET, SOCK_DGRAM)

    def start(self):
        try:
            print('Start Udp Server')
            print('Bind Udp:{}'.format(self.Addr))
            self.Socket.bind(self.Addr)
        except Exception as e:
            print('Error bind Udp:', e)
            exit(1)
        try:
            print('Loop waiting for messages...')
            while True:
                data, addr = self.Socket.recvfrom(self.BufSize)
                print('[{}:{}] {}'.format(addr[0], addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Remote->Local:{}'.format(data.decode('utf-8')))

                info = '{}'.format(data.decode('utf-8'))
                self.Socket.sendto(info.encode('utf-8'), addr)
                print('[{}:{}] {}'.format(self.Addr[0], self.Addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Local->Remote:{}'.format(info))
        finally:
            self.Socket.close()

    def stop(self):
        self.Socket.close()
        print('Stop Udp Server')


def start_udp_server(host, port):
    s = UdpServer(host=host, port=port)
    s.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch tcp server listen, such as \'127.0.0.1\'', type=str, default='0.0.0.0')
    parser.add_argument(
        '-p', '--port', help='port: port number witch tcp server listen, such as \'6001\'', type=int, default=6001)
    args = parser.parse_args()
    start_udp_server(host=args.ip, port=args.port)
