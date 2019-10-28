import argparse
import concurrent.futures as futures
import os
import time
from socket import *


class TcpClient:
    def __init__(self, host='127.0.0.1', port=6000):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.tcpClientSocket = socket(AF_INET, SOCK_STREAM)

    def start(self):
        try:
            print('Start Tcp Client')
            self.tcpClientSocket.connect(self.Addr)
            pass
        except Exception as e:
            print('Error connect to server:', e)
            os._exit(1)

    def send(self, data):
        Addr = self.tcpClientSocket.getsockname()
        print('[{}:{}] {}'.format(Addr[0], str(Addr[1]), time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        print('Local->Remote:{}'.format(data))
        self.tcpClientSocket.send(data.encode('utf-8'))

    def recv(self):
        try:
            while True:
                data = self.tcpClientSocket.recv(self.BufSize)
                if not data:
                    break
                print('[{}:{}] {}'.format(self.Addr[0], str(self.Addr[1]), time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Remote->Local:{}'.format(data.decode('utf-8')))
        finally:
            print('Remote host forcibly closed connect:{}'.format(self.Addr))
            self.tcpClientSocket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch tcp client connect, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch tcp client connect, such as \'6000\'', type=int, default=6000)
    args = parser.parse_args()
    c = TcpClient(host=args.ip, port=args.port)
    c.start()
    futures.ThreadPoolExecutor(max_workers=1).submit(c.recv)

    while True:
        data = input()
        if not data:
            print('Remote host forcibly closed connect:{}'.format(c.Addr))
            c.tcpClientSocket.close()
            break
        c.send(data)
