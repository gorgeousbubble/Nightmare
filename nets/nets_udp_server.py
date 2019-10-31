#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from socket import *


class UdpServer:
    def __init__(self, host='', port=6001):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.udpServerSocket = socket(AF_INET, SOCK_DGRAM)

    def start(self):
        try:
            print('Start Udp Server')
            print('Bind Udp:{}'.format(self.Addr))
            self.udpServerSocket.bind(self.Addr)
        except Exception as e:
            print('Error bind Udp:', e)
            os._exit(1)
        try:
            print('Loop waiting for messages...')
            while True:
                data, addr = self.udpServerSocket.recvfrom(self.BufSize)
                print('[{}:{}] {}'.format(addr[0], addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Remote->Local:{}'.format(data.decode('utf-8')))

                info = '{}'.format(data.decode('utf-8'))
                self.udpServerSocket.sendto(info.encode('utf-8'), addr)
                print('[{}:{}] {}'.format(self.Addr[0], self.Addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Local->Remote:{}'.format(info))
        finally:
            self.udpServerSocket.close()


if __name__ == '__main__':
    s = UdpServer()
    s.start()
