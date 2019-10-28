import os
import time
from socket import *


class UdpClient:
    def __init__(self, host='127.0.0.1', port=6001):
        self.Host = host
        self.Port = port
        self.BufSize = 4096
        self.Addr = (self.Host, self.Port)
        self.udpClientSocket = socket(AF_INET, SOCK_DGRAM)

    def start(self):
        try:
            print('Start Udp Client')
            while True:
                data = input()
                if not data:
                    break

                self.udpClientSocket.sendto(data.encode('utf-8'), self.Addr)
                print('[{}:{}] {}'.format(self.Addr[0], self.Addr[1], time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Local->Remote:{}'.format(data))
                data, addr = self.udpClientSocket.recvfrom(self.BufSize)
                if not data:
                    break
                print('[{}:{}] {}'.format(addr[0], str(addr[1]), time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                print('Local->Remote:{}'.format(data))
        except Exception as e:
            print('Error send messages:', e)
        finally:
            self.udpClientSocket.close()


if __name__ == '__main__':
    c = UdpClient()
    c.start()
