import concurrent.futures as futures
import time
from socket import *


class TCPServer:
    def __init__(self, host='', port=6000):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.Clients = []
        self.Executor = futures.ThreadPoolExecutor(max_workers=3)
        self.tcpServerSocket = socket(AF_INET, SOCK_STREAM)
        self.tcpServerSocket.bind(self.Addr)
        print('Start Tcp Server')
        print('Listen Tcp:{}'.format(self.Addr))
        self.tcpServerSocket.listen(5)

    def start(self):
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
                    print('[{}] {}'.format(tcpClientAddr, time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                    print('Remote->Local:{}'.format(data.decode('utf-8')))
                    for v in self.Clients:
                        sock = v[0]
                        addr = v[1]
                        if sock == tcpClientSocket:
                            info = '{}'.format(data.decode('utf-8'))
                            sock.send(info.encode('utf-8'))
                else:
                    print('Remote host forcibly closed connect:{}'.format(
                        tcpClientAddr))
                    self.Clients.remove((tcpClientSocket, tcpClientAddr))
                    break
        finally:
            tcpClientSocket.close()


if __name__ == '__main__':
    s = TCPServer()
    s.start()
