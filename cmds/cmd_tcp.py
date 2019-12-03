#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import concurrent.futures as futures
from nets import TcpServer
from nets import TcpClient


def parse_cmd_tcp(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--ip', help='ip address: ipv4 address witch tcp server listen, such as \'127.0.0.1\'', type=str,default='127.0.0.1')
    sub_parser.add_argument('-p', '--port', help='port: port number witch tcp server listen, such as \'6000\'', type=int, default=6000)
    sub_parser.add_argument('-m', '--mode', help='mode: tcp mode choose, \'s\' or \'server\' indicate tcp server, \'c\' or \'client\' indicate tcp client', type=str, default='server')
    args = cmd_parser.parse_args()
    print(args)
    # choose tcp mode
    if args.mode == 'server' or args.mode == 's':
        s = TcpServer(host=args.ip, port=args.port)
        s.start()
    elif args.mode == 'client' or args.mode == 'c':
        c = TcpClient(host=args.ip, port=args.port)
        c.start()
        futures.ThreadPoolExecutor(max_workers=1).submit(c.recv)
        while True:
            try:
                data = input()
                if not data:
                    c.tcpClientSocket.close()
                    break
                c.send(data)
            except:
                c.tcpClientSocket.close()
                break
    else:
        print('Invalid Tcp Mode. You can input \'c\' stand for \'client\' or \'s\' for \'server\'.')
