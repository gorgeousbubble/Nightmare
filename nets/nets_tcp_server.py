import concurrent.futures as futures
import os
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
        self.tcpServerSocket = socket(AF_INET, SOCK_STREAM)

    def start(self):
        try:
            print('Start Tcp Server')
            print('Listen Tcp:{}'.format(self.Addr))
            self.tcpServerSocket.bind(self.Addr)
            self.tcpServerSocket.listen(5)
        except Exception as e:
            print('Error listen Tcp:', e)
            os._exit(1)
        while True:
            print('Loop waiting for connect...')
            tcpClientSocket, tcpClientAddr = self.tcpServerSocket.accept()
            self.Executor.submit(self.recv, tcpClientSocket, tcpClientAddr)
            print('Success accept client:{}'.format(tcpClientAddr))
            self.Clients.append((tcpClientSocket, tcpClientAddr))

    def recv(self, tcpClientSocket, tcpClientAddr):
        try:
            while True:
                data = tcpClientSocket.recv(self.BufSize)
                if data:
                    print('[{}:{}] {}'.format(tcpClientAddr[0], tcpClientAddr[1], time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                    print('Remote->Local:{}'.format(data.decode('utf-8')))
                    for v in self.Clients:
                        sock = v[0]
                        addr = v[1]
                        if sock == tcpClientSocket:
                            print('[{}:{}] {}'.format(self.Addr[0], str(self.Addr[1]), time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                            print('Local->Remote:{}'.format(data.decode('utf-8')))
                            info = '{}'.format(data.decode('utf-8'))
                            sock.send(info.encode('utf-8'))
                else:
                    break
        finally:
            print('Remote host forcibly closed connect:{}'.format(tcpClientAddr))
            self.Clients.remove((tcpClientSocket, tcpClientAddr))
            tcpClientSocket.close()


if __name__ == '__main__':
    s = TcpServer()
    s.start()
